t=int(input())
for i in range(t):
    s=input()
    c=input()
    if c in s:
        lst=s.split(c)
    print(lst)    
    count=0     
    for i in range(len(lst)):
        if((len(lst[i]))%2==0):
            count+=1
    if(count==2):
        print("yes")  
    else:
        print("no")    
        