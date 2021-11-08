import matplotlib.pyplot as plt
import random
import numpy

data=[]
colors=[]
centers=[[1,3,"bo"],[3,1,"bo"],[1,1,"r+"],[3,3,"r+"]]
colors=["r+","bo"]
for sector in centers:
  for x in range(50):
    data.append([sector[0]+random.randint(-11,11)/10,sector[1]+random.randint(-11,11)/10])
    colors.append(sector[2])
for n in range(200):
  plt.plot(data[n][0], data[n][1], colors[n])

  
plt.savefig("random_data")