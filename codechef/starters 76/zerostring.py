T=int(input())
for a in range(T):
    n=int(input()) #4
    s=input()      #1101    0010
    one=0
    for i in range(n): #for counting number of 1s
        if(s[i]=="1"):
            one+=1
    zero=n-one
    if(one>zero):
        print(1+zero)
    else:
        print(one)    
