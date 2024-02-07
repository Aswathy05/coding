t=int(input())
for i in range(t):
    n=int(input())
    s=input()
    i=0
    str1=""
    while(True):
        if(s[i]=="U"):
            str1+="D"
            i+=1
        elif(s[i]=="D"):
            str1+="U"
            i+=1
        elif(s[i]=="L"):
            str1+="LR"
            i+=2  
        if(i==n):
            break
    print(str1)            

