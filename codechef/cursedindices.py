t=int(input())
for i in range(t):
    n=int(input())
    s1=input().split()
    s=[]
    for i in s1:
        s.append(int(i))
    s.sort()
    count=0
    for i in range(n):
        if(sum(s[:i])>=s[i]):
            ind=i
            count+=1
            break
    if(count==0):
        print(0)
    else:        
        cursed=s[i:]
        cursedNum=len(s[i:])    
        print(cursedNum)
    for i in s:
        print(i, end=" ") 
    print()       
    