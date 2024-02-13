import sys
sys.stdin=open("input.txt","r")
sys.stdout=open("output.txt","w")
t=int(input())
for i in range(t):
    n,q=(int(i) for i in input().split())
    s=list(input())
    count=1
    lst=[]
    for i in range(len(s)-1):
        if(s[i]==s[i+1]):
            count+=1    
        else:
            lst.append(count) 
            count=1             
    step=[max(lst)]  
    for i in range(q):
        c=input()
        s.append(c)  
        if(s[len(s)-1]==s[len(s)-2]):
            count+=1
            lst[len(lst)-1]=count
        step.append(max(lst))
    print(*step)    





