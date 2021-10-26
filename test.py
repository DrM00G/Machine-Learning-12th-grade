
from node import Node 
from neuralnetwork2 import NeuralNet
nodes=[]
for i in range(5):
  nodes.append(Node(i))
nodes[0].input_bool="X"
nodes[1].input_bool="Y"
nodes[4].output_bool=True
connections=[(0,2,0.6),(0,3,0.4),(1,2,-0.5),(1,3,-0.3),(2,4,0.2),(3,4,-0.1)]

data=[[1,2,"+"],[1,4,"+"],[2,2,"+"],[2,1,"−"],[3,2,"−"],[4,1,"−"]]


nn=NeuralNet(nodes,connections,0.001)
# print(nn.pred_value((1,2,"+")))
# for point in data:
#   print(str(nn.pred_value(point))+","+str(point))
for i in range(20000):
  nn.update(data)
print(nn.pred_value((1,2,"+")))

