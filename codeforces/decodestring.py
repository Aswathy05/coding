q=int(input())
for i in range(q):
    n=int(input())
    t=input()
    d={}
    alp=list("abcdefghijklmnopqrstuvwxyz")
    for i in range(26):
        d[i]=alp[i] 
    t1=t[::-1]   
    j=0
    s=""
    while(True):
        num=""
        if(j==len(t)):
            break    
        elif(t1[j]=="0" and (len(t)-j)>=2):
            num+=str(t1[j+2])
            num+=str(t1[j+1])
            s+=d[int(num)-1]
            j+=3
        else:
            s+=d[int(t1[j])-1]
            j+=1   
    print(s[::-1])        


            
