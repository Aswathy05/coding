t=int(input())
for i in range(t):
    a=input().split()
    n=int(a[0])          #no of digits of str1
    d=int(a[1])         #insertion digit
    str1=input()    #digit
    res=0
    for j in range(n):
        if(int(str1[j])<d):
            print(str1[:j]+str(d)+str1[j:])
            res=1
            break
    if(res==0):
        print(str1+str(d))

