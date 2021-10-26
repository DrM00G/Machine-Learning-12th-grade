from node import Node 
from neuralnetwork3 import NeuralNet
nodes=[]
for i in range(4):
  nodes.append(Node(i))
nodes[0].input_bool="X"
nodes[1].input_bool="Y"
nodes[2].input_bool="bias"
nodes[3].output_bool=True
connections=[(0,3,1),(1,3,1),(2,3,1)]

data=[[1,2,"+"],[1,4,"+"],[2,2,"+"],[2,1,"−"],[3,2,"−"],[4,1,"−"]]
nn=NeuralNet(nodes,connections,0.001,1,1)
# print(nn.pred_value((1,2,"+")))
# for point in data:
#   print(str(nn.pred_value(point))+","+str(point))
# for i in range(20000):
nn.update(data)
print(nn.connections)
