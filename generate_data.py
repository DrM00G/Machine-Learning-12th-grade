import matplotlib.pyplot as plt
import random
import numpy

data=[]
centers=[[1,3,"bo"],[3,1,"bo"],[1,1,"r+"],[3,3,"r+"]]
colors=["r+","bo"]

for x in range(500):
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
  plt.plot(point[0]/20, point[1]/20, color)
plt.savefig("random_data")