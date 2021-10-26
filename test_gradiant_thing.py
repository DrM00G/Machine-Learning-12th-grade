import time
import matplotlib.pyplot as plt
import numpy
from node import Node 
from neuralnetwork4 import NeuralNet
nodes=[]



times=[]
for layers in range(4):
  print(layers+1)
  for i in range((2*(layers+1))+1):
    nodes.append(Node(i))
  nodes[0].input_bool="X"
  nodes[1].input_bool="Y"
  nodes[(layers+1)*2].output_bool=True
  connections=[]
  for level in range(layers):
    for j in range(2):
      for k in range(2):
        connections.append((level*2+j,level*2+2+k,1))
  for i in range(2):
    connections.append(((layers)*2+i,(layers+1)*2,1))
  data=[(1,2,"-")]
  start = time.time()
  def f(x):
    return numpy.arctan(x)

  def f_prime(x):
    return 1/(1+(x**2))

  nn=NeuralNet(nodes,connections,0.001,f,f_prime)
  for i in range(10000):
    nn.update(data)
  times.append(time.time()-start)


# for i in range(5):
#   nodes.append(Node(i))
# nodes[0].input_bool="X"
# nodes[1].input_bool="Y"
# nodes[4].output_bool=True
# connections=[(0,2,1),(0,3,1),(1,2,1),(1,3,1),(2,4,1),(3,4,1)]
# data=[(1,2,"-")]
# start = time.time()

# def f(x):
#   return x**2 

# def f_prime(x):
#   return 2*x

# nn=NeuralNet(nodes,connections,0.001,f,f_prime)

# nn.update(data)
print(times)
plt.plot([x for x in range(1,len(times)+1)], times)
plt.savefig('net_times.png')