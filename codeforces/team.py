n=int(input())  #no of problems
count=0
for i in range(n):
    x,y,z=tuple([int(a) for a in input().split()])
    if(x==1 and y==1):
        count+=1
    elif(y==1 and z==1):
        count+=1
    elif(z==1 and x==1):
        count+=1
print(count)                 
        