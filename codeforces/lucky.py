t=int(input())
for i in range(t):
    lst=input()
    lst1,lst2=[],[]
    for i in lst[:((len(lst))//2)]:
        lst1.append(int(i))
    for i in lst[((len(lst))//2):]:
        lst2.append(int(i))    
    if(sum(lst1)==sum(lst2)):
        print("yes")    
    else:
        print("no")    