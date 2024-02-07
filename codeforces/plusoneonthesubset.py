t=int(input())
for i in range(t):
    n=int(input())
    a=input().split()
    lst=[]
    for j in a:
        lst.append(int(j))  
    for j in range(n):
        if(lst[j]==min(lst)):
            print(max(lst)-lst[j])
            break
        