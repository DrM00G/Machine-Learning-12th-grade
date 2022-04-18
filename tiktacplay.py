from tiktacminmax import MinMax
from tictactoerecombiningtree import TikTacTree
import random

class RandomFella:
  def __init__(self,turn):
    self.turn=turn

  def make_move(self,state):
    options=[]
    for n in range(9):
      if state[n]=="0":
        options.append(n)

    move=random.choice(options)
    new_state=[]
    for i in range(9):
      if i == move:
        new_state.append(self.turn)
      else:
        new_state.append(state[i])
    return new_state



        
def check_win(state):
    if check_same(state, 0, 1, 2):
      return state[0]
    elif check_same(state, 3, 4, 5):
      return state[3]
    elif check_same(state, 6, 7, 8):
      return state[6]
    elif check_same(state, 0, 4, 8):
      return state[0]
    elif check_same(state, 2, 4, 6):
      return state[6]
    elif check_same(state, 0, 3, 6):
      return state[0]
    elif check_same(state, 1, 4, 7):
      return state[1]
    elif check_same(state, 2, 5, 8):
      return state[2]
    elif "0" not in state:
      return "3"
    else:
      return False

def check_same(state,uno,dos,tres):
    if state[uno]==state[dos] and state[dos]==state[tres] and state[uno]!='0':
      return True
    else:
      return False

def make_str(state):
    return str(state[0]+state[1]+state[2]+state[3]+state[4]+state[5]+state[6]+state[7]+state[8])

score=[0,0]
game=TikTacTree()
players_round1=[MinMax(game.node_dict,"x"),RandomFella("o")]
players_round2=[RandomFella("x"),MinMax(game.node_dict,"o")]

for n in range(25):
  print("round "+str(n)+": "+str(score))
  state="000000000"
  turn_count=0
  while check_win(state)==False:
    state=make_str(players_round1[turn_count%2].make_move(state))
    turn_count+=1
    if check_win(state)=='x':
      score[0]+=1
    if check_win(state)=='o':
      score[1]+=1

for n in range(25):
  print("round "+str(n+25)+": "+str(score))
  state="000000000"
  turn_count=0
  while check_win(state)==False:
    state=make_str(players_round2[turn_count%2].make_move(state))
    turn_count+=1
    if check_win(state)=='o':
      score[0]+=1
    if check_win(state)=='x':
      score[1]+=1
print(score)
    
    
    
  