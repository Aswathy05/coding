t=int(input())
for i in range(t):
    n=int(input())
    s=input()
    count=0
    for i in range(len(s)):
        for j in s[i:]:
            print(j)
            if(s[i]==j):
                lst=s.split(s[i])
                print(lst)
                for k in lst:
                    if(k==''):
                        count+=1
    print(count)                    

