#Transpose of a given matrix using List comprehension

mat = [[1,2,3],[4,5,6],[7,8,9]]
tran = [[mat[j][i] for j in range(len(mat))]for i in range(len(mat[0]))]
print(tran)