t=int(input())
for i in range(t):
    lst=input().split()
    s1=int(lst[0])
    s2=int(lst[1])
    s3=int(lst[2])
    s4=int(lst[3])
    max1,max2=max(s1,s2),max(s3,s4)
    lst1=[]
    for i in lst:
        lst1.append(int(i))
    if(max(max1,max2)==max(lst1)):
        lst1.remove(max(lst1))
        if(min(max1,max2)==max(lst1)):
            print("yes")
        else:
            print("no")    
    else:
        print("no")        