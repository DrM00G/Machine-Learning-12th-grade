class Node:
  def __init__(self,tree,state,parents,turn):
    self.tree=tree
    self.state=state
    self.parents=parents
    self.turn=turn 
    self.turn_options=["x",'o']
    self.children=self.produce()

  def reproduce(self):
    # child_states=self.produce()
    child_nodes=[Node(self.tree,child_state,[self],self.turn_options[self.turn_options.index(self.turn)-1]) for child_state in self.produce()]
    recombine_list=[]
    for child in child_nodes:
      if self.tree.make_str(child.state) not in self.tree.node_dict.keys():
        self.tree.node_dict[self.tree.make_str(child.state)]=child
        recombine_list.append(child)
      else:
        self.tree.node_dict[self.tree.make_str(child.state)].parents.append(self)
    # final_list=[child for child in recombine_list]
    for child in recombine_list:
      child.reproduce()
    # for child in child_states:

  

  def produce(self):
    next_states=[]
    if self.check_win(self.state)==False:
      for n in range(9):
        if self.state[n] == "0":
          new_state=[]
          for i in range(9):
            if i!=n:
              new_state.append(self.state[i])
            else:
              new_state.append(self.turn)
          next_states.append(new_state)
    return next_states

  def check_win(self,state):
    if self.check_same(state, 0, 1, 2):
      return state[0]
    elif self.check_same(state, 3, 4, 5):
      return state[3]
    elif self.check_same(state, 6, 7, 8):
      return state[6]
    elif self.check_same(state, 0, 4, 8):
      return state[0]
    elif self.check_same(state, 2, 4, 6):
      return state[6]
    elif self.check_same(state, 0, 3, 6):
      return state[0]
    elif self.check_same(state, 1, 4, 7):
      return state[1]
    elif self.check_same(state, 2, 5, 8):
      return state[2]
    elif "0" not in state:
      return "3"
    else:
      return False

  def check_same(self,state,uno,dos,tres):
    if state[uno]==state[dos] and state[dos]==state[tres] and state[uno]!='0':
      return True
    else:
      return False
    
          
        
      

class TikTacTree:
  def __init__(self):
    self.node_dict={}
    self.node_dict["000000000"]=Node(self,['0','0','0','0','0','0','0','0','0'],[],"x")
    # print(len(first.reproduce()))
    self.node_dict["000000000"].reproduce()
      # self.node_dict[self.make_str(node.state)]=node
    # print(self.node_dict.keys())

    
    
  def make_str(self,state):
    return str(state[0]+state[1]+state[2]+state[3]+state[4]+state[5]+state[6]+state[7]+state[8])

# print("start")
# do_shit= TikTacTree()
