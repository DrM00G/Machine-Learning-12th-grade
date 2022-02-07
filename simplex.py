import numpy as np
mat_sys=[[3,2,5,1,0,0,0,55],[2,1,1,0,1,0,0,26],[1,1,3,0,0,1,0,30],[5,2,4,0,0,0,1,57],[20,10,15,0,0,0,0,0]]

def test_bottom_row(mat):
  for spot in range(len(mat[4])-1):
    if mat[4][spot] > 0:
      return True
  return False

def det_pivot_col(mat):
  pivot=0
  for spot in range(len(mat[4])-1):
    if mat[4][spot] > mat[4][pivot]:
      pivot=spot

  return pivot

def det_pivot_row(mat,col):
  pivot=0
  for spot in range(len(mat)-1):
    # print(str(mat[spot][col])+"/"+str(mat[spot][7])+":"+str(mat[spot][col]/mat[spot][7]))
    if (mat[spot][7]/mat[spot][col]) < (mat[pivot][7]/mat[pivot][col]):
      if((mat[spot][7]/mat[spot][col])>0):
        print(str((mat[spot][7]/mat[spot][col]))+">"+str((mat[pivot][7]/mat[pivot][col])))
        pivot=spot
  return pivot

def normalize(mat,average,row):
  new_mat=mat
  for col in range(len(mat[row])):
    new_mat[row][col]=(mat[row][col]/average)
  return new_mat

def pivot_mat(mat,col,row):
  new_mat=mat
  for chg_row in mat:
    if mat.index(chg_row)!=row:
      divide_value=chg_row[col]/mat[row][col]
      for chg_col in range(len(chg_row)):
        new_mat[mat.index(chg_row)][chg_col]=chg_row[chg_col]-(mat[row][chg_col]*divide_value)
  return(new_mat)

# while test_bottom_row(mat_sys):
for i in range(3):
  print("------------------")
  pivot_col=det_pivot_col(mat_sys)
  pivot_row=det_pivot_row(mat_sys,pivot_col)
  mat_sys=normalize(mat_sys,mat_sys[pivot_row][pivot_col],pivot_row)
  mat_sys=pivot_mat(mat_sys,pivot_col,pivot_row)
  print("col: "+str(pivot_col)+" row: "+str(pivot_row))
  for row in mat_sys:
    print(row)