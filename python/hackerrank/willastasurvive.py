t=int(input())
for i in range(t):
    lst=input().split()
    a=int(lst[0])
    b=int(lst[1])
    if(a>b):
        if((a-b)%10==0):
            print((a-b)//10)
        else:
            print(((a-b)//10)+1)
    elif(b>a):
        if((b-a)%10==0):
            print((b-a)//10)
        else:
            print(((b-a)//10)+1)  
    else:
        print(0)    