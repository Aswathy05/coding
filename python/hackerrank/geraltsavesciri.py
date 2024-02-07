t=int(input())
for i in range(t):
    n=int(input())          #no of monsters
    x=int(input())          #attacking power
    lst=[]
    for j in range(n):
        h=int(input())     #hit point of nth monster
        lst.append(h)
    count=0    
    lst1=[]
    for j in lst:
        while(j>=0):
            j-=2*x
        count+=1
        lst1.append(count)
    count1=0    
    for j in lst1:
        count1+=int(j)
    print(count1)    

