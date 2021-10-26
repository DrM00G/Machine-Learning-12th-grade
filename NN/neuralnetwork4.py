
class NeuralNet:
  def __init__(self,node_set,connections,alpha,f,f_prime):
    self.alpha=alpha
    self.node_set=node_set
    self.connections=connections
    self.f=f
    self.f_prime=f_prime
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
      error=0
      for input in data:
        if self.pred_value(input)!=input[2]:
          inputs=[self.node_input(x,input) for x in self.node_set]
          outputs=[self.node_output(x,input) for x in self.node_set]
          self.update_ngrads(outputs,inputs)
          error+=self.node_set[i[1]].gradiant*self.f_prime(inputs[i[1]])*outputs[i[0]]
          # print(str(i)+"   "+str(error))
      new_weights.append([i[0],i[1],i[2]-self.alpha*error])
    # print(new_weights)
    self.connections=new_weights
    self.update_relations()

  def update_ngrads(self,outputs,inputs):
    for node in self.node_set[::-1]:
      if node.output_bool:
        node.gradiant=self.f_prime(outputs[node.index])
      else:
        gradiant=0
        for child in node.children:
          gradiant+=child[0].gradiant*self.f_prime(inputs[child[0].index])*child[1]
        node.gradiant=gradiant


  def pred_value(self,data):
    value=self.node_output(self.output_node,data)
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

  def node_input(self,node,inputs):
    value_count=0
    for parent in node.parents:
      value_count+=(self.node_output(parent[0],inputs)*parent[1])
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
    elif node.input_bool=="bias":
      return 1
      
  def node_output(self,node,inputs):
    value_count=0
    for parent in node.parents:
      value_count+=(self.node_output(parent[0],inputs)*parent[1])
    if node.input_bool==False:
      # print("node:"+str(node.index))
      # print(value_count)
      return self.f(value_count)
    elif node.input_bool=="X":
      # print("node:"+str(node.index))
      # print(inputs[0])
      # print(inputs)
      return self.f(inputs[0])
    elif node.input_bool=="Y":
      # print("node:"+str(node.index))
      # print(inputs[1])
      return self.f(inputs[1])
    elif node.input_bool=="bias":
      return self.f(1)
