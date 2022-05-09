import matplotlib.pyplot as plt


def generate_next(input):
  counts=[1]
  differnts=[str(input)[0]]
  count=0
  for i in range(len(str(input))-1):
    if str(input)[i+1]==str(input)[i]:
      counts[count]+=1
    else:
      differnts.append(str(input)[i+1])
      counts.append(1)
      count+=1
  output_list=[str(counts[0])+differnts[0]]
  for n in range(len(counts)-1):
    output_list.append(output_list[len(output_list)-1]+str(counts[n+1])+differnts[n+1])
  return(output_list[len(output_list)-1])

loopers=[]
if generate_next(0)==str(10):
  print("well, at least that works?")
for n in range(5000000):
  if generate_next(n) == str(n):
    print("BINGO: "+str(n))
    loopers.append(n)
  if n%100000 == 0:
    print(n)
    print(generate_next(n))
    print("-----------")
print("Nope :/")
print(loopers)

# sequence=[1]
# for n in range(20):
#   sequence.append(generate_next(sequence[len(sequence)-1]))
# # print(sequence)
# plt.plot(range(50),range(50))
# plt.plot(range(21),sequence)
# plt.axis((0,50,0,50))
# plt.savefig("looksaysequence")
# print("done son")