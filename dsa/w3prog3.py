def transpose(m):
    r=len(m)
    c=len(m[0])
    trans=[]
    for i in range(c):
        row=[]
        for j in range(r):
            row.append(0)
        trans.append(row)        
    for i in range(r):
        for j in range(c):
            trans[j][i]=m[i][j]
    return(trans)     
print(transpose([[3]]))

