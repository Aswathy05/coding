a=input().split()
k=int(a[0]) #117
r=int(a[1]) #3
x=1
while((k*x)%10!=r):
    if((k*x)%10==0):
        break
    x+=1
print(x)    

