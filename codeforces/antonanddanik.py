n=int(input())
s=input()
A,D=0,0
for i in s:
    if(i=="A"):
        A+=1
    elif(i=="D"):
        D+=1
if(A>D):
    print("Anton")
elif(D>A):
    print("Danik")    
else:
    print("Friendship")