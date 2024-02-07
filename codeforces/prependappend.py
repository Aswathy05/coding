t=int(input())
for i in range(t):
    n=int(input()) #length of final string
    s=input() #string
    while(s[0]!=s[len(s)-1]):
        s=s[1:len(s)-1]
        if(len(s)==0):
            break
    print(len(s))