x=input().split()
n,x=int(x[0]),int(x[1])
count=x
dis=0
for i in range(n):
    y=input().split()
    if(y[0]=="-"):
        if(count<int(y[1])):
            dis+=1
        else:
            count-=int(y[1])    
    if(y[0]=="+"):
        count+=int(y[1])
print(count,dis)        
    