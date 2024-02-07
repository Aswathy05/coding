t=int(input())
for i in range(t):
    lst=input().split()
    lst1=[]
    for i in lst:
        lst1.append(int(i))
    lst1.remove(max(lst1))    
    lst1.remove(min(lst1))
    print(lst1[0])