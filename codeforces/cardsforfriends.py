t=int(input())
for i in range(t):
    lst=input().split()
    w=int(lst[0])
    h=int(lst[1])
    n=int(lst[2])
    if(n==1):
        print("yes")
    else:
        count=1
        while(w%2==0 or h%2==0):
            if(w%2==0):
                w//=2
                count*=2
            else:
                h//=2    
                count*=2
        if(count>=n):
            print("yes")     
        else:
            print("no")    