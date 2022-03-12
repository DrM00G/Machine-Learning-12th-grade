import random
import matplotlib.pyplot as plt
# import numpy as np

class TikTacToe:
  def __init__(self,strat_num):
    strat_num=strat_num
    strats=[]
    possible_states=self.create_state(["0","0","0","0","0","0","0","0","0"],"1")
    for state in self.create_state(["0","0","0","0","0","0","0","0","0"],"2"):
      # if state not in possible_states:
      possible_states.append(state)
    # print(len(possible_states))

    # str_states=[self.make_str(state) for state in possible_states]
    step={self.make_str(state):0 for state in possible_states}
    reduced_states = [self.make_list(state) for state in step.keys()]
    str_states=[self.make_str(state) for state in reduced_states]
    # reduced_states = [self.make_list(state) for state in str_states]
    for n in range(strat_num):
      strats.append({state:0 for state in str_states}) #here
      for i in range(len(reduced_states)):
        possible_choices=[]
        for spot in range(len(reduced_states[i])):
          if reduced_states[i][spot]=="0":
            possible_choices.append(spot)
        # print(possible_choices)
        strats[len(strats)-1][self.make_str(reduced_states[i])]=random.choice(possible_choices)
    # print(len(strats[0].keys()))
    # print(strats[0]["000000000"])
    # print(self.match_up(['0','0','0','0','0','0','0','0','0'], strats[0], strats[1]))
    print("start tourny")
    original_gen=[]
    previous_gen=[]
    origin_comparison=[]
    previous_comparison=[]
    for strat in strats:
      previous_gen.append(strat)
      original_gen.append(strat)
    for n in range(20):
      strats=self.next_gen(strats)
      previous_comparison.append(self.compare_gens(strats[0:5],previous_gen))
      origin_comparison.append(self.compare_gens(strats[0:5],original_gen))
      previous_gen=[]
      for strat in strats:
        previous_gen.append(strat)
      
    # plt.subplots()
    fig, ax = plt.subplots()
    ax.plot([n for n in range(20)], previous_comparison, linewidth=2.0)
    

    # plt.plot(origin_comparison, range(20))
    plt.savefig('tikbestvsprevious.png')
      # for strat in strats:
      #   print("------------")
      #   for n in range(5):
      #     print(strat[str_states[n]])
    print("done did")
    best_child=strats[0]

    
  def compare_gens(self,group_1,group_2):
    score=[0 for n in range(len(group_1))]
    for n in range(len(group_1)):
      for strat in group_2:
        outcome_1=self.check_win(self.match_up(['0','0','0','0','0','0','0','0','0'], group_1[n], strat))
        outcome_2=self.check_win(self.match_up(['0','0','0','0','0','0','0','0','0'], strat, group_1[n]))
        if outcome_1=="1":
          score[n]+=1
        elif outcome_1=="2":
          score[n]-=1
        if outcome_2=="2":
          score[n]+=1
        elif outcome_2=="1":
          score[n]-=1
    return sum(score)/len(score)
        
        

  def next_gen(self,strats):
    best=self.tournament(strats)
    # print(best)
    new_strats=[strats[n] for n in best]
    babies=[]
    for first in range(len(new_strats)):
      for second in range(len(new_strats)):
        if first!=second:
          babies.append(self.breed(new_strats[first],new_strats[second]))
          #add babies to original then blast
    for baby in babies:
      new_strats.append(baby)
    return new_strats
    


  def breed(self,strat_1,strat_2):
    child={}
    for state in strat_1.keys():
      option=[strat_1[state],strat_2[state]]
      child[state]=random.choice(option)
    return child
      

  def tournament(self,strats):
    score=[0 for n in range(len(strats))]
    size=len(strats)
    for first in range(len(strats)):
      # print(first)
      for second in range(len(strats)):
        if first!=second:
          winner=self.check_win(self.match_up(['0','0','0','0','0','0','0','0','0'], strats[first], strats[second]))
          if winner=="1":
            score[first]+=1
            score[second]-=1
          elif winner=="2":
            score[first]-=1
            score[second]+=1
    top=[]
    for i in range(5):
      best=[-10*size,0]
      for n in range(len(score)):
        if n not in top:
          if score[n]>best[0]:
            best[0]=score[n]
            best[1]=n
      top.append(best[1])
    print(score)
    return top
      
      
  def create_state(self,previous,turn):
    pos_states=[]
    # print(pos_states)
    if self.check_win(previous)==False:
      pos_states.append(previous)
      for n in range(len(previous)):
        if previous[n]=="0":
          perhaps_state=[]
          for i in previous:
            perhaps_state.append(i)
          perhaps_state[n]=turn
          if turn=="2":
            next_turn="1"
          else:
            next_turn="2"
          
          for state in self.create_state(perhaps_state, next_turn):
            pos_states.append(state)
    
      
    return pos_states
          
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

  def match_up(self,state,strat_1,strat_2):
    # state=[0,0,0,0,0,0,0,0,0]
    # print(state)
    if self.check_win(state) == False:
      new_state=[]
      
      change_index=strat_1[self.make_str(state)]
      for spot in range(9):
        if spot!=change_index:
          new_state.append(state[spot])
        else:
          new_state.append("1")
      # print("new state:")
      # print(new_state)
      return self.inverse_state(self.match_up(self.inverse_state(new_state),strat_2,strat_1))
    else:
      return state
      


  def make_str(self,state):
    return str(state[0]+state[1]+state[2]+state[3]+state[4]+state[5]+state[6]+state[7]+state[8])

  def make_list(self,state):
    return [n for n in state]
  
  def inverse_state(self,state):
    inverse=[]
    for spot in state:
      if spot=="1":
        inverse.append("2")
      elif spot=="2":
        inverse.append("1")
      else:
        inverse.append("0")
    return inverse
  
tiktac=TikTacToe(25)