t=int(input())
for i in range(t):
    n=int(input())
    s=list(input())
    count=0
    lst=[]
    for j in s:
        if j not in lst:
            lst.append(j)
            count+=2
        else:
            count+=1
    print(count)            
