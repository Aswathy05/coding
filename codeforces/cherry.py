t=int(input())
for i in range(t):
    n=int(input())
    s=input().split()
    lst=[]
    for i in s:
        lst.append(int(i))
    maxi=max(lst)    
    for i in lst:
        if(i==maxi):
            lst.remove(i)           2cfqf
    print(lst)
    mini=max(lst)
    print(mini)
    print(maxi*mini)