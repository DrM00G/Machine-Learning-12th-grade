from tictactoerecombiningtree import TikTacTree

import random
class NeuralNet:
  def __init__(self,weights,mute_rate):
    self.mutation_rate=mute_rate
    self.weights=weights
    self.network=self.network_setup()
    
  def network_setup(self):
    network=[[],[],[],[],[Node([],38,output=True)]]
    
    for n in range(4):
      network[3].append(Node(network[4],33+n))      
    network[3].append(Node(network[4],37,bias=True))

    for n in range(8):
      network[2].append(Node(network[3],24+n))
    network[2].append(Node(network[3],32,bias=True))
    
    for n in range(14):
      network[1].append(Node(network[2],n+9))
    network[1].append(Node(network[2],23,bias=True))
    #0-8
    #0,1,3,4>9
    #1,2,4,5>10
    #3,4,6,7>11
    #4,5,7,8>12
    #0-8>13

      
    kids=[[network[1][0],network[1][9],network[1][13]],
    [network[1][1],network[1][9],network[1][10],network[1][13]],
    [network[1][2],network[1][10],network[1][13]],
    [network[1][3],network[1][9],network[1][11],network[1][13]],
    [network[1][4],network[1][9],network[1][10],network[1][11],network[1][12],network[1][13]],
    [network[1][5],network[1][10],network[1][12],network[1][13]],
    [network[1][6],network[1][11],network[1][13]],
    [network[1][7],network[1][11],network[1][12],network[1][13]],
    [network[1][8],network[1][12],network[1][13]]
    ]
    for n in range(9):
      network[0].append(Node(kids[n],n,input=True))

    return network
  
          

    

  def calculate(self,input_state):
    for layer in self.network:
      for node in layer:
        node.input_value=0
        node.final=0
    for i in range(9):
      self.network[0][i].input=input_state[i]
    for layer in self.network:
      for node in layer:
        if node.output==False:
          for child in node.children:
            weight=self.weights[str(node.index)+","+str(child.index)]
            if node.bias==False:
              child.input+=node.af(node.input)*weight
            else:
              child.input+=1*weight
        else:
          return node.af(node.input)
        
    
        
    

    
class Node:
  def __init__(self,children, index, input=False,output=False,bias=False):
    self.children=children
    self.input=input
    self.output=output
    self.bias=bias
    self.index=index
    self.input_value=0
    self.final=0

  def af(self,input):
    #temp, idk the activation function
    return input
    

def generate_network_edges():
  net=NeuralNet(0,0)
  edges=[]
  for layer in net.network:
    for node in layer:
      for child in node.children:
        edges.append(str(node.index+","+str(child.index)))
  return edges

class NeuralPlayer:
  def __init__(self,net):
    self.net=net
    self.tree=TikTacTree(4)
    self.weighted_tree=self.weigh(self.tree.node_dict)

  def weigh(self,tree):
    weighted_tree={}
    for key in tree.keys():
      weighted_tree[key]=[0,tree[key]]
    next_nodes=[]
    for key in tree.keys():
      if len(tree[key].children)==0:
        weighted_tree[key][0]=self.net.calculate(key)
        for parent in tree[key].parents:
          next_nodes.append(parent)
    for key in next_nodes:
      weighted_tree[key][0]=sum([weighted_tree[child.state][0] for child in tree[key].children])
      for parent in tree[key].parents:
        next_nodes.append(parent)
      
        

first_gen_nets = []

for beginner in range(30):
  weights={}
  for edge in generate_network_edges():
    weights[edge]=random.uniform(-0.2,0.2)
  first_gen_nets.append(NeuralNet(weights,0.5))



