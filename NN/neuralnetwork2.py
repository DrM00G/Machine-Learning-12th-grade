
class NeuralNet:
  def __init__(self,node_set,connections,alpha):
    self.alpha=alpha
    self.node_set=node_set
    self.connections=connections
    self.update_relations()
    for node in self.node_set:
      if node.output_bool==True:
        self.output_node=node
      
  def update_relations(self):
    for node in self.node_set:
      node.children=[]
      node.parents=[]
    for i in self.connections:
      self.node_set[i[0]].children.append((self.node_set[i[1]],i[2]))
      self.node_set[i[1]].parents.append((self.node_set[i[0]],i[2]))

  def update(self,data):
    new_weights=[]
    for i in self.connections:
      error_sum=0
      for input in data:
        if self.pred_value(input)!=input[2]:
          weight_prod=self.path_add(i)
          n_i=self.node_value(self.node_set[i[0]],input)
          y_pred=2*self.node_value(self.output_node,input)   
          error_sum+=weight_prod*n_i*y_pred
          # if i[0]==3 and i[1]==4:
          #   print(str(weight_prod)+str(n_i)+str(y_pred)+str(input))
      new_weights.append([i[0],i[1],i[2]-self.alpha*error_sum])
    # print(new_weights)
    self.connections=new_weights
    self.update_relations()

  def pred_value(self,data):
    value=self.node_value(self.output_node,data)
    if value>0:
      return("+")
    else:
      return("-")

  def path_add(self,connection):
    path_addition=0
    for children in self.node_set[connection[1]].children:
      path_addition+=self.path_add((connection[1],children[0].index,children[1]))*children[1]
    if self.node_set[connection[1]].output_bool==True:
      return 1
    else:
      return path_addition
      
  def node_value(self,node,inputs):
    value_count=0
    for parent in node.parents:
      value_count+=(self.node_value(parent[0],inputs)*parent[1])
    if node.input_bool==False:
      # print("node:"+str(node.index))
      # print(value_count)
      return value_count
    elif node.input_bool=="X":
      # print("node:"+str(node.index))
      # print(inputs[0])
      return inputs[0]
    elif node.input_bool=="Y":
      # print("node:"+str(node.index))
      # print(inputs[1])
      return inputs[1]
    print("HELP")
