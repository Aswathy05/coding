t=int(input())
for j in range(t):
    n=int(input())
    lst1=input().split()
    count=0
    lst=[]
    for i in lst1:
        lst.append(int(i))
    eve,odd=0,0   
    for i in lst:
        if(eve>0 and odd>0):
            break
        if(i%2==0):
            eve+=1
        else:
            odd+=1  
    if(n%2!=0 and odd>0):
        print("yes")
    elif(eve>0 and odd>0):
        print("yes")
    else:
        print("no")