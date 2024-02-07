n=int(input())
for i in range(n):
    a=input()
    if(len(a)>10):
        x=a[0]
        y=len(a[1:len(a)-1])
        z=a[len(a)-1]
        print(x,y,z,sep="")
    else:
        print(a)    