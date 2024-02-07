t=int(input())
for i in range(t):
    n=int(input())
    s=list(input())
    lst=[]
    while(True):
        count=0
        for i in range(len(s)):
            count+=1
            if(s[i] in s[i+1:]):
                j=count
                lst.append(s[i])  
                s=s[j:]
                print(lst,s)
                break    
        if(len((set(s)))==len(s)):
            break
    for i in lst:
        print(i,end="")      
    print()               