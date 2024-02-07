t=int(input())
for i in range(t):
    s=list(input())
    pi=list("314159265358979323846264338327")
    count=0
    for j in range(len(s)):
        if(s[j]!=pi[j]):
            break
        count+=1
    print(count)    
        