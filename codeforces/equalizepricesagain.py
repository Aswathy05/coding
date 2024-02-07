q=int(input())
for i in range(q):
    n=int(input())
    a=input().split()
    lst=[]
    for i in a:
        lst.append(int(i))
    if(sum(lst)//n)==(sum(lst)/n):
        print(sum(lst)//n)   
    else:
        print((sum(lst)//n)+1)          