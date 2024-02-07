t=int(input())
for i in range(t):
    n=int(input())
    s=input()
    lst=["T","i","m","u","r"]
    count=0
    if(n==5):
        for i in s:
            if i in lst:
                count+=1
                lst.remove(i)
        if(count==5):
            print("yes")        
        else:
            print("no")   
    else:
        print("no")         