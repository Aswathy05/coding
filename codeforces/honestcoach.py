t=int(input())
for i in range(t):
    n=int(input())
    s=input().split()
    lst=[]
    for i in s:
        lst.append(int(i))
    lst.sort()
    lst1=[]
    for i in range(len(lst)-1):
        if(lst[i]>lst[i+1]):
            lst1.append(lst[i]-lst[i+1])
        else:
            lst1.append(lst[i+1]-lst[i])  
    print(min(lst1))
                