n=int(input())
count=0
for i in range(n):
    p=input()
    if(p=="Tetrahedron"):
        count+=4
    elif(p=="Cube"):
        count+=6 
    elif(p=="Octahedron"):
        count+=8
    elif(p=="Dodecahedron"):
        count+=12
    elif(p=="Icosahedron"):
        count+=20
print(count)                 