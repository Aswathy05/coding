#compute addition and multiplication with add_mat(m1,m2) and mul_mat(m1,m2)
def add_mul(a,b):
    summat = [[a[i][j]+b[i][j] for j in range(len(a[0]))]for i in range(len(a))]
    return summat
def mul_mat(a,b):
    prodmat = [[sum([a[i][k]*b[k][j] for k in range(len(b))]) for j in range(len(b[0]))] for i in range(len(a))]
    return prodmat
m1 = [[1,2,3],[4,5,6],[7,8,9]]
m2 = [[9,8,7],[6,5,4],[3,2,1]]

summat = add_mul(m1,m2)
print("Sum:", summat)

prodmat = mul_mat(m1,m2)
print("Product:", prodmat)