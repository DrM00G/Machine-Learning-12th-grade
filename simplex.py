import numpy as np
mat_sys=[[3,2,5,1,0,0,0,55],[2,1,1,0,1,0,0,26],[1,1,3,0,0,1,0,30],[5,2,4,0,0,0,1,57],[20,10,15,0,0,0,0,0]]

class SimplexSolver:
  def __init__(self,mat_sys):
    self.mat_sys=mat_sys

  def test_bottom_row(self,mat):
    for spot in range(len(mat[len(mat)-1])-1):
      if mat[len(mat)-1][spot] > 0:
        return True
    return False

  def det_pivot_col(self,mat):
    pivot=0
    for spot in range(len(mat[len(mat)-1])-1):
      if mat[len(mat)-1][spot] > mat[len(mat)-1][pivot]:
        print(spot)
        pivot=spot
    return pivot

  def det_pivot_row(self,mat,col):
    pivot=0
    for spot in range(len(mat)-1):
      if (mat[spot][len(mat[spot])-1]/mat[spot][col]) < (mat[pivot][len(mat[spot])-1]/mat[pivot][col]):
        if((mat[spot][len(mat[spot])-1]/mat[spot][col])>0):
          print(str((mat[spot][len(mat[spot])-1]/mat[spot][col]))+">"+str((mat[pivot][len(mat[spot])-1]/mat[pivot][col])))
          pivot=spot
    return pivot

  def normalize(self,mat,average,row):
    new_mat=mat
    for col in range(len(mat[row])):
      new_mat[row][col]=(mat[row][col]/average)
    return new_mat

  def pivot_mat(self,mat,col,row):
    new_mat=mat
    for chg_row in mat:
      if mat.index(chg_row)!=row:
        divide_value=chg_row[col]/mat[row][col]
        for chg_col in range(len(chg_row)):
          new_mat[mat.index(chg_row)][chg_col]=chg_row[chg_col]-(mat[row][chg_col]*divide_value)
    return(new_mat)

  def solve(self):
    while(self.test_bottom_row(self.mat_sys)):
      pivot_col=self.det_pivot_col(self.mat_sys)
      print(pivot_col)
      pivot_row=self.det_pivot_row(self.mat_sys,pivot_col)
      # print("pivot: "+str(pivot_col)+","+str(pivot_row))
      self.mat_sys=self.normalize(self.mat_sys,self.mat_sys[pivot_row][pivot_col],pivot_row)
      self.mat_sys=self.pivot_mat(self.mat_sys,pivot_col,pivot_row)
      for row in simplex.mat_sys:
        print(row)


test_mat=[[2,1,1,1,0,0,14],[4,2,3,0,1,0,28],[2,5,5,0,0,1,30],[1,2,-1,0,0,0,0]]
new_mat=[[2,1,0,1,0,0,10],[1,2,-2,0,1,0,20],[0,1,2,0,0,1,5],[-2,1,-2,0,0,0,0]]
simplex=SimplexSolver(new_mat)
simplex.solve()
# for row in simplex.mat_sys:
#   print(row)