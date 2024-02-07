t=int(input())
for i in range(t):
    lst=input().split()
    a=int(lst[0])
    b=int(lst[1])
    if(a>b):
        num=a-b 
    else:
        num=b-a  
    count=0
    for i in range(10,0,-1):
        if(num>i):
            count+=num//i
            num%=i
    print(count)  
