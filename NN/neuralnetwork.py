class NeuralNet:
  def __init__(self,node_set,connections,alpha):
    self.node_set=node_set
    self.connections=connections
    for connection in connections:
      self.node_set[connection[0]].child.append(self.node_set[connection[1]])
    self.alpha=alpha

  def update(self,connection):
    levels=[[] for i in self.node_set]
    levels[0].append((self.node_set[connection[1]],len(self.node_set[connection[1]].children)))
    for level in range(len(levels)):
      if levels[level]!=[]:
        for node in levels[level]:
          i=0
          for child in node.children:
            i+=len(child.children)
            levels[level+1].append((child,i))
    for i in range(len(levels)):
      if levels[i]==[]:
        top_level=i-1
    prod_weights=0
    for child in levels[top_level]:
      prod_weights+=self.calculate_path(levels,top_level,levels[top_level].index(child))
    n_i=self.node_set[connection[0]].value(self.connections)
    y_pred=self.node_set[len(self.node_set)-1].value(self.connections)
    return y_pred*prod_weights*n_i
    
  def calculate_path(self,levels,current,node_index):
    if current>0:
      for parent in levels[current-1]:
        if parent[1]-1>=node_index:
          for connection in self.connections:
            if connection[0]==parent[0].index and connection[1]==levels[current][node_index].index:
              parent_weight=connection[2]
              return parent_weight*self.calculate_path(levels,current-1,levels[current-1].index(parent))
    else:
      return 1