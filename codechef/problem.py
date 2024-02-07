t=int(input())
for i in range(t):
    lst=input().split()
    a=int(lst[0])
    b=int(lst[1])
    a1=a
    b1=b
    while(True):
        if(a>b):
            a-=1
            b+=1
        elif(b>a):
            b-=1
            a+=3
        if(a==b):
            print("yes")
            break 
        elif(a==a1 or b==b1):
            print("no")
            break  

