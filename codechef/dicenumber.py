t=int(input())
for i in range(t):
    x=input().split()
    lst=[]
    for i in x:
        lst.append(int(i))
    lst1=sorted(lst[:3])
    lst2=sorted(lst[3:])    
    lst1=lst1[::-1]
    lst2=lst2[::-1]
    a,b="",""
    for i in lst1:
        a+=str(i)
    for i in lst2:
        b+=str(i)
    if(a>b):
        print("Alice")
    elif(a<b):
        print("Bob")
    else:
        print("Tie")                