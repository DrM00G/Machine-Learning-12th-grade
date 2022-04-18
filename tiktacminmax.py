from tictactoerecombiningtree import TikTacTree

class MinMax:
  def __init__(self,tree,order='x'):
    self.tree=tree
    # print("for the love of christ"+str(len(self.tree.keys())))
    self.order=order
    self.weighted_tree=self.weigh(self.tree)

  def make_move(self,state):
    max=[-10000000,0]
    for n in range(len(self.tree[state].children)):
      if max[0]< self.weighted_tree[self.make_str(self.tree[state].children[n])][0]:
        max=[self.weighted_tree[self.make_str(self.tree[state].children[n])][0],self.weighted_tree[self.make_str(self.tree[state].children[n])][1]]
    return max[1].state
    

  def weigh(self,tree):
    new_tree={}
    finish_states=[]
    for key in tree.keys():
      if self.check_win(tree[key].state) == self.order:
        new_tree[key]=[1,tree[key]]
        finish_states.append(key)
      elif self.check_win(tree[key].state) == False or self.check_win(tree[key].state) == '3':
        new_tree[key]=[0,tree[key]]
      else:
        new_tree[key]=[-1,tree[key]]
        finish_states.append(key)
    # print("check point 1")
    for key in finish_states:
      # print(len(finish_states))
      for parent in self.tree[key].parents:
        new_tree[self.make_str(parent.state)][0]+=new_tree[key][0]
        if self.make_str(parent.state) not in finish_states:
          finish_states.append(self.make_str(parent.state))
    # print("check point 2")
    return new_tree
        
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

  def make_str(self,state):
    return str(state[0]+state[1]+state[2]+state[3]+state[4]+state[5]+state[6]+state[7]+state[8])

game=TikTacTree()
minmax=MinMax(game.node_dict)