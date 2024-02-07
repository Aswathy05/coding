t=int(input())
score=0
for i in range(t):
    s=input().split()
    s=s[2:]
    lst1=[]
    i=0
    while(True):
        if(s[i]=="|"):
            break
        lst1.append(s[i])
        i+=1
    lst2=s[i+1:]
    count=-1
    for i in lst1:
        if(i in lst2):
            count+=1 
    if(count!=-1):         
        score+=(2**count)        
print(score)        
