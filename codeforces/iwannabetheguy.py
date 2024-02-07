n=int(input())
p=input().split()
q=input().split()
lst=p[1:]+q[1:]
a=[]
for i in lst:
    if int(i) not in a:
        a.append(int(i))
a.sort()        
b=[]
for i in range(1,n+1):
    b.append(i)    
if(a==b):
    print("I become the guy.")    
else:
    print("Oh, my keyboard!")
    
