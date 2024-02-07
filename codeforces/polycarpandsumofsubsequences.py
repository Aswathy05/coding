t=int(input())
for i in range(t):
    a=input().split()
    lst=[]
    for i in a:
        lst.append(int(i))
    count1=lst[0]+lst[1]+lst[2]
    count2=lst[0]+lst[1]+lst[3]
    if(count1==max(lst)):
        print(lst[0],lst[1],lst[2])
    elif(count2==max(lst)):
        print(lst[0],lst[1],lst[3])