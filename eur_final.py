import numpy as np
import math
data=[(1,2),(3,4),(4,5)]
trans_data=[]
for coord in data:
  trans_data.append((coord[0],coord[1]**2))
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


initial_ab=[1,0]
alpha=0.01
RSSA=[]
RSSB=[]
for coord in data:
  RSSA.append(2*((np.sqrt(initial_ab[0]*coord[0]+initial_ab[1]))-coord[1])*((((initial_ab[0]*coord[0]+initial_ab[1])**(-0.5))/2)*coord[0]))
  RSSB.append(2*((np.sqrt(initial_ab[0]*coord[0]+initial_ab[1]))-coord[1])*((((initial_ab[0]*coord[0]+initial_ab[1])**(-0.5))/2)))
initial_ab[0]-=sum(RSSA)*alpha
initial_ab[1]-=sum(RSSB)*alpha
print("RSSA: "+str(sum(RSSA)))
print("RSSB: "+str(sum(RSSB)))

print(initial_ab)