import numpy as np
import random
import matplotlib.pyplot as plt


class NeuralNet:
  def __init__(self,training_set,weights,mute_rate):
    self.mutation_rate=mute_rate
    self.weights=weights
    self.normalized_set=self.normalize_set(training_set)
    self.network=[[],[],[],[],[Node([],24,output=True)]]
    for n in range(3):
      self.network[3].append(Node(self.network[4],20+n))
    self.network[3].append(Node(self.network[4],23,bias=True))
    for n in range(6):
      self.network[2].append(Node(self.network[3],13+n))
    self.network[2].append(Node(self.network[3],19,bias=True))
    for n in range(10):
      self.network[1].append(Node(self.network[2],n+2))
    self.network[1].append(Node(self.network[2],12,bias=True))
    self.network[0].append(Node(self.network[1],0,input=True))
    self.network[0].append(Node(self.network[1],1,bias=True))

  def calculate(self,input):
    for level in self.network:
      for node in level:
        node.input_value=0
        node.final=0
    self.network[0][0].calculate(self.weights,input)
    self.network[0][1].calculate(self.weights)
    return(self.network[4][0].final)

  def calc_rss(self):
    values=[]
    for point in self.normalized_set:
      values.append((point[1]-self.calculate(point[0]))**2)
    
    return sum(values)
    
    
    
  
  def normalize_set(self, set):
    max_x=-1000000
    max_y=[1000000,-1000000]
    
    for point in set:
      if point[0]>max_x:
        max_x=point[0]
      if point[1]>max_y[1]:
        max_y[1]=point[1]
      if point[1]<max_y[0]:
        max_y[0]=point[1]
    return [(point[0]/max_x,2*((point[1]-max_y[0])/max_y[1])-0.5) for point in set]  


class Node:
  def __init__(self,children, index, input=False,output=False,bias=False):
    self.children=children
    self.input=input
    self.output=output
    self.bias=bias
    self.index=index
    self.input_value=0
    self.final=0

  def tanf(self,x):
    # print(x)
    return np.tanh(x)
    # (((np.exp(x))-(np.exp(-x)))/((np.exp(x))+(np.exp(-x))))

  def calculate(self,weights,input=False):
    if self.output==False:
      if self.input==True:
        self.input_value=input
      if self.bias==False:
        output=self.tanf(self.input_value)
      else:
        output=1
      for child in self.children:
        if child.bias==False:
          weighted_output=weights[str(self.index)+","+str(child.index)]*output
          # print(str(self.index)+": "+str(weighted_output))
          child.input_value+=weighted_output
      if self.index in [1,12,19,23]:
        for child in self.children:
          child.calculate(weights)
    else:
      self.final = self.tanf(self.input_value)

    
        

def generate_network_edges(layers, bias = True):
  bias_node = 1 if bias else 0
  edges = []

  for depth in range(len(layers)-1):
    stagger1 = sum([layers[k] for k in range(depth)])+(depth*bias_node)
    stagger2 = sum([layers[k] for k in range(depth+1)])+((depth+1)*bias_node)
    for i in range(layers[depth]+bias_node):
      for j in range(layers[depth+1]):
        edges.append((stagger1+i,stagger2+j))
  return edges

def order_sets(set):
  ordered=[]
  for i in range(15):
    top=[10000000,0]
    for net in set:
      if net.calc_rss()<top[0] and net not in ordered:
        top=[net.calc_rss(),net]
    ordered.append(top[1])
  # print(set.index(ordered[0]))
  # print([net.calc_rss() for net in set])
  return ordered


  
training=[(0.0, 7), (0.2, 5.6), (0.4, 3.56), (0.6, 1.23), (0.8, -1.03),
 (1.0, -2.89), (1.2, -4.06), (1.4, -4.39), (1.6, -3.88), (1.8, -2.64),
 (2.0, -0.92), (2.2, 0.95), (2.4, 2.63), (2.6, 3.79), (2.8, 4.22),
 (3.0, 3.8), (3.2, 2.56), (3.4, 0.68), (3.6, -1.58), (3.8, -3.84),
 (4.0, -5.76), (4.2, -7.01), (4.4, -7.38), (4.6, -6.76), (4.8, -5.22)]




# print(generate_network_edges([1,10,6,3,1]))


#START TEST CODE
test_weights={}
for edge in generate_network_edges([1,10,6,3,1]):
  test_weights[str(edge[0])+","+str(edge[1])]=0.1
  TikTacNet=NeuralNet(training,test_weights,0.5)

def expected_output(w,i):
  return np.tanh(3*w*np.tanh(6*w*np.tanh(10*w*np.tanh(w*np.tanh(i)+w)+w)+w)+w)

# print("expected value: "+str(expected_output(0.1,0)))
# print(TikTacNet.calculate(0))

# print("output node 0: "+str(np.tanh(0)))

# print("output node 2-11: "+str(np.tanh(np.tanh(0)+np.tanh(1))))

# x=10*np.tanh(2*np.tanh(0))
# x_2=np.tanh(1)
# # print(x)
# y=np.tanh(x+x_2)
# print("13-18 node outputs: "+str(y))

# print("20-22 node outputs: "+str(np.tanh(6*y+x_2)))

# q=np.tanh(6*y+x_2)

# print("output: "+str(np.tanh(3*q+x_2)))

# print(np.tanh(y))





#START REAL CODE
net_weights=[]

for n in range(30):
  weights={}
  for edge in generate_network_edges([1,10,6,3,1]):
    weights[str(edge[0])+","+str(edge[1])]=random.uniform(-0.2,0.2)
  
  # net_weights[n].append(weights)
  
  TikTacNet=NeuralNet(training,weights,0.5)
  net_weights.append(TikTacNet)

print('start analysis')




ordered_nets=order_sets(net_weights)

print("begining rss "+str(ordered_nets[0].calc_rss()))

rsses=[ordered_nets[0].calc_rss()]



# x_values=[point[0] for point in ordered_nets[0].normalized_set]

# values=[[] for n in range(15)]
# for i in range(15):
#   for point in ordered_nets[i].normalized_set:
#     values[i].append(ordered_nets[i].calculate(point[0]))

# for value in values:
#   plt.plot(x_values,value)


# plt.savefig("compare_gen1_nets")








for gen in range(10):
  
  new_set=[]
  # print([key for key in ordered_nets[0].weights.keys()])
  # print("0,5"+str([diction.weights["0,5"] for diction in ordered_nets]))
  # print("5,16:"+str([diction.weights["5,16"] for diction in ordered_nets]))
  
  
  # print("calc 1"+str([diction.calculate(0) for diction in ordered_nets]))
  # print(/n)
  for net in ordered_nets:
    flawed_clone={}
    for key in net.weights.keys():
      flawed_clone[key]=net.weights[key]+net.mutation_rate*np.random.normal(0,1)
    new_mut_rate=net.mutation_rate*np.exp((np.random.normal(0,1))/(2**(0.5)*len(net.weights.keys())**0.25))
    new_set.append(NeuralNet(training,flawed_clone,new_mut_rate))
    new_set.append(net)
  
  ordered_nets=order_sets(new_set)
  print("next rss "+str(ordered_nets[0].calc_rss()))
  rsses.append(ordered_nets[0].calc_rss())
print("final rss "+str(ordered_nets[0].calc_rss()))

plt.plot(range(11),rsses)

plt.savefig("numbernet_rss")