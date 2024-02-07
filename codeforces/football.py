n=input()
zero,one=0,0
for i in range(len(n)):
    if(n[i]=="1"):
        one+=1
    else:
        zero+=1
    if(i!=len(n)-1 and (n[i]!=n[i+1] )):
        one=0
        zero=0
    if(i==(len(n)-1)):
        if(n[i]!=n[i-1]):
            one,zero=0,0
    print(one,zero)        
    if(one==7 or zero==7):
        print("YES")
        break
else:
    print("NO")           