import random
origin_table={"1,false":{"stop":1,"continue":1,"mulligan":1},
      "1,true":{"stop":1,"continue":1},
      "2,false":{"stop":2,"continue":1,"mulligan":1},
      "2,true":{"stop":2,"continue":1},
      "3,false":{"stop":3,"continue":1,"mulligan":1},
      "3,true":{"stop":3,"continue":1},
      }
alpha=0.001
def Q(state,action,next_state,table):
  current_rating=table[state][action]
  max_a=-10000
  if int(next_state[0])<=3:
    for action_opt in table[next_state]:
      if table[next_state][action_opt]>max_a:
        max_a=table[next_state][action_opt]
  else:
    max_a=-3
  return current_rating+(alpha*(max_a-current_rating))

def run_round(previous,start,table):
  if start==True:
    previous=random.randint(1,3)
  next_move=random.randint(1,3)
  # print(table[str(previous)+",false"])
  table[str(previous)+",false"]["continue"]=Q(str(previous)+",false","continue",str(previous+next_move)+",false",table)
  if previous+next_move<=3:
    return(run_round(previous+next_move,False,table))
  else:
    # for i in table:
    #   print(table[i])
    return(table)
      
    

# print(Q("1,false","mulligan","3,true"))
for i in origin_table:
  print(origin_table[i])

for n in range(10001):
  origin_table=run_round(0,True,origin_table)
  if n%1000 ==0:
    print("---------"+str(n))
    for i in origin_table:
      print(origin_table[i])
