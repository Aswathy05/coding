t=int(input())
for i in range(t):
    s=input()
    for i in range(len(s)):
        ind=int(len(s)/2)
        if(s[:ind]==s[ind:]):
            print("yes")
            break
        else:
            print("no")    
            break