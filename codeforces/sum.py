t=int(input())
for j in range(t):
    n=input().split()
    lst=[]
    for i in n:
        lst.append(int(i))
    maxi=max(lst)  
    lst.remove(max(lst))
    if(sum(lst)==maxi):
        print("yes")
    else:
        print("no")    