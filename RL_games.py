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

def run_round(state,table,count):

#CHANGE SO IT CHANGES NEXT THING TO BE MUILIGAIN
  
  next_state=[0,0,"false"]
  
  if state==0:
    state=[random.randint(1,3),random.choice(["continue","mulligan"]),"false"]
  if state[1]=="mulligan" or state[2]=="true":
    next_state[2]="true"

  next_state[0]=random.randint(1,3)
  if next_state[2]=="false":
    next_state[1]=random.choice(["continue","mulligan"])#continue from line 46
  else:
    next_state[1]="continue"

  if state[1]=="continue":
    table[str(state[0]+count)+","+state[2]][state[1]] = Q(str(state[0]+count)+","+state[2],state[1],str(state[0]+next_state[0]+count)+","+next_state[2],table)
    count+=state[0]
  else:
    table[str(state[0]+count)+","+state[2]][state[1]] = Q(str(state[0]+count)+","+state[2],state[1],str(next_state[0]+count)+","+next_state[2],table)
  if next_state[0]+count<=3:
    return(run_round(next_state,table,count))
  else:
    return(table)  


    
    

# print(Q("1,false","mulligan","3,true"))
for i in origin_table:
  print(origin_table[i])

for n in range(10001):
  origin_table=run_round(0,origin_table,0)
  if n%1000 ==0:
    print("---------"+str(n))
    for i in origin_table:
      print(origin_table[i])
