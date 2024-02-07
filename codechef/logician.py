t=int(input())
for i in range(t):
    n=int(input())
    s1=input()
    s=[]
    for i in s1:
        s.append(int(i))
    no=0    
    for i in range(n):
        if(s[i]==0):
            no=1
            print("NO")
        elif(s[i]==1 and no!=1 and i<(n-1)):
            print("IDK")
        elif(s[i]==1 and no==1):
            print("NO")
        elif(s[i]==1 and i==(n-1) and no!=1):
            print("YES")            
