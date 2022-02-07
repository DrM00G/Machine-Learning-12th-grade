import numpy as np
class PCA:
  def __init__(self,dimension):
    data=0
    self.eigens=[]
    self.dimension=dimension

  def fit(self, data):
    restructured_data=[[] for n in range(self.dimension)]
    for dim in range(self.dimension):
      for point in data:
        restructured_data[dim].append(point[dim])
    #   averages.append(sum(restructured_data[dim])/len(restructured_data[dim]))
    print("restructured")


    cor_coefs=[[] for i in range(self.dimension)]
    for i in range(self.dimension):
      for j in range(self.dimension):
        if i!=j:
          cor_coefs[i].append(np.corrcoef([restructured_data[i],restructured_data[j]])[1][0])
          # print(str(i)+" cor "+str(j))
          # print(cor_coefs[i])

        else:
          cor_coefs[i].append(1)
    print("Found cors")

    final_matrix=np.matrix(cor_coefs)
    print("MATRIX OBJECT:")
    # print(cor_coefs)
    self.eigens=np.linalg.eig(final_matrix)


# test_pca=PCA(3)

# test_pca.fit([[1,2,0],[2,3,1],[2,1,3],[3,4,2],[3,2,4],[4,3,6]])
# print("result:")
# print(test_pca.eigens)


        
    
    