import numpy as np
import math
data=[(1,1),(2,2),(3,9),(4,16)]
trans_data=[]
for coord in data:
  trans_data.append((np.log(coord[0]),np.log(coord[1])))
outputs=[[y[1]] for y in trans_data]
inputs=[[1,x[0]] for x in trans_data]
Y=np.array(outputs)
X=np.array(inputs)
# X_inv = np.pinv(X)
inner=np.dot(np.transpose(X),X)
# print(inner)
inner2=np.linalg.inv(inner)
# print(inner2)
B=np.dot(np.dot(inner2,np.transpose(X)),Y)
print(B)

rss_count1=[]
for coord in data:
  rss_count1.append(((math.e**B[0])*(coord[0]**B[1])-coord[1])**2)

rss_count2=[]
for coord in data:
  firstest=coord[0]
  first=firstest**2.48
  fx=0.5*first
  rss_count2.append((fx-coord[1])**2)

print(sum(rss_count1))
print(sum(rss_count2))


initial_ab=B
alpha=0.0001
RSS=[]
for coord in data:
  RSS.append(((B[0]*(coord[0]**B[1]))-coord[1])**2)
print("Old RSS: "+str(sum(RSS)))

for n in range(20000):
  RSSA=[]
  RSSB=[]
  for coord in data:
    RSSA.append(2*(initial_ab[0]*(coord[0]**initial_ab[1])-coord[1])*(coord[0]**initial_ab[1]))
    RSSB.append(2*(initial_ab[0]*(coord[0]**initial_ab[1])-coord[1])*((coord[0]**initial_ab[1])*np.log(initial_ab[1])*initial_ab[0]))
  initial_ab[0]-=sum(RSSA)*alpha
  initial_ab[1]-=sum(RSSB)*alpha
  RSS=[]
  for coord in data:
    RSS.append((initial_ab[0]*(coord[0]**initial_ab[1])-coord[1])**2)
print("New RSS: "+str(sum(RSS)))
print("A,B: "+str(initial_ab[0])+","+str(initial_ab[1]))

new_data=[(0.5,0.5),(1,3),(3,10),(5,20),(10,60),(100,10000)]


print("NEW F(X)")

initial_ab=[1,1]
alpha=0.0001
RSS=[]
for coord in data:
  RSS.append(((initial_ab[0]*(initial_ab[1]**coord[0]))-coord[1])**2)
print("Old RSS: "+str(sum(RSS)))

for n in range(20000):
  RSSA=[]
  RSSB=[]
  for coord in data:
    RSSA.append(2*(initial_ab[0]*(initial_ab[1]**coord[0])-coord[1])*(initial_ab[1]**coord[0]))
    RSSB.append(2*(initial_ab[0]*(initial_ab[1]**coord[0])-coord[1])*(initial_ab[0]*coord[0]*(initial_ab[1]**(coord[0]-1))))
    #FIX THESE EQUASIONS FOR THE WEDNESDAY
  initial_ab[0]-=sum(RSSA)*alpha
  initial_ab[1]-=sum(RSSB)*alpha
  RSS=[]
  for coord in data:
    RSS.append((initial_ab[0]*(coord[0]**initial_ab[1])-coord[1])**2)
print("New RSS: "+str(sum(RSS)))
print("A,B: "+str(initial_ab[0])+","+str(initial_ab[1]))