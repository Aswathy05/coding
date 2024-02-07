t=int(input())
for i in range(t):
    n=int(input())
    a=input().split()
    lst=[]
    for i in a:
        lst.append(int(i))   
    mini=min(lst)  
    count=0  
    """ minsum=0
    for i in lst:
        if(i==mini):
            minsum+=i
            count1+=1 """
    for i in lst:
        if(i>mini):
            count+=1
    print(count)        

