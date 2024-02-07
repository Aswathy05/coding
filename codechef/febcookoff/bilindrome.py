t=int(input())
for i in range(t):
    n=int(input()) #length of the string
    s=input()       #string
    res=-1
    for j in range(n):
        for k in range(j+1,n):
            if(s[j]==s[k]):    
                res=n-2
    print(res)
