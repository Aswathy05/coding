t=int(input())
for i in range(t):
    x=input().split()
    n=int(x[0])
    lst=x[1]
    intlst=int(x[1])
    revlst=lst[::-1]
    last3=""
    if(n>3):
        for i in range(0,3):
            last3+=str((revlst[i])) 
        last3=(last3[::-1]) 
        last3lst=list(last3)
        if(int(last3)%8==0):
            print(intlst)
        else:
            for i in range(3):
                if(last3lst[i]=="0"):
                    last3lst[i]="1"    
            last3int=""
            for i in last3lst:
                last3int+=i

            lstnew=lst[:n-3]+last3int
            lstnew=int(lstnew)
            last3int=int(last3int)
            if(last3int%8!=0):
                lstnew+=(last3int%8)
            print(lstnew)  
    else:
        case1=intlst%8
        case2=(8-(case1))
        if(case1>case2):
            print(intlst+case2) 
        elif(case1<=case2):
              print(intlst+case1)
        elif(intlst%8==0):
            print(intlst)
            


        