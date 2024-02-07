t=int(input())
for j in range(t):
    n=int(input())
    s=input()
    count=0
    if(n==1):
        print("Ramos")
    else:    
        while(True):
            initcount=count
            for i in range (len(s)-1):
                if(s[i]!=s[i+1]):
                    s.remove(s[i+1])
                    s.remove(s[i])
                    count+=1
                    break 
            if(initcount==count or len(s)==0):
                break
        if(count%2==0):
            print("Ramos")  
        else:
            print("Zlatan")