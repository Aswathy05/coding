t=int(input())
for i in range(t):
    lst=input().split()
    count=0
    for i in lst:
        count+=int(i)
    if(count>=2):
        print("Not now")    
    else:
        print("Water filling time")    