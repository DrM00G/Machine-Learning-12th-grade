import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
import random
# import sklearn

data_points=[]
data_colors=[]
centers=[[1,3,"bo"],[3,1,"bo"],[1,1,"r+"],[3,3,"r+"]]
colors=["r+","bo"]

for x in range(200):
  closeness=100000000000
  color=0
  point=[random.randint(0,100),random.randint(0,100)]
  for spot in centers:
    if closeness>=((spot[0]-point[0]/20)**2+(spot[1]-point[1]/20)**2):
      color=spot[2]
      closeness=((spot[0]-point[0]/20)**2+(spot[1]-point[1]/20)**2)
  dice=random.randint(0,50**2)
  if dice<closeness**2:
    color=colors[colors.index(color)-1]
  data_points.append([point[0]/20, point[1]/20])
  data_colors.append(color)


test_data_points=[]
test_data_colors=[]
for x in range(200):
  closeness=100000000000
  color=0
  point=[random.randint(0,100),random.randint(0,100)]
  for spot in centers:
    if closeness>=((spot[0]-point[0]/20)**2+(spot[1]-point[1]/20)**2):
      color=spot[2]
      closeness=((spot[0]-point[0]/20)**2+(spot[1]-point[1]/20)**2)
  dice=random.randint(0,50**2)
  if dice<closeness**2:
    color=colors[colors.index(color)-1]
  test_data_points.append([point[0]/20, point[1]/20])
  test_data_colors.append(color)

accuracy=[]

for k in range(20):
  neigh = KNeighborsClassifier(n_neighbors=k)
  neigh.fit(data_points, data_colors)
  count=0
  for n in range(200):
    if neigh.predict(test_data_points[n]) == test_data_colors[n]:
      count+=1
  plt.plot(count/200,k)
plt.savefig("knn data")

