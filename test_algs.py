import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
import random
from sklearn import tree
# import sklearn

data=[]
colors=[]
centers=[[1,3,"bo"],[3,1,"bo"],[1,1,"r+"],[3,3,"r+"]]
# colors=["r+","bo"]
for sector in centers:
  for x in range(50):
    data.append([sector[0]+random.randint(-12,12)/10,sector[1]+random.randint(-12,12)/10])
    colors.append(sector[2])
# for n in range(200):
#   plt.plot(data[n][0], data[n][1], colors[n])

  
# plt.savefig("random_data")


test_data=[]
test_colors=[]
centers=[[1,3,"bo"],[3,1,"bo"],[1,1,"r+"],[3,3,"r+"]]
# colors=["r+","bo"]
for sector in centers:
  for x in range(50):
    test_data.append([sector[0]+random.randint(-11,11)/10,sector[1]+random.randint(-11,11)/10])
    test_colors.append(sector[2])

accuracy=[]
tally=[[],[]]
for k in range(50):
  # print(len(data))
  # print(len(colors))
  neigh = KNeighborsClassifier(n_neighbors=(k+1)*2)
  neigh.fit(data,colors)
  count=0
  for n in range(200):
    if neigh.predict([test_data[n]]) == test_colors[n]:
      count+=1
  # print(k)
  # print(count)
  tally[0].append(count/200)
  tally[1].append(k*2)
  # print(count/200)
plt.plot(tally[1],tally[0],"b")
plt.savefig("knn data")

clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, Y)