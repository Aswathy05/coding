t=int(input())
for i in range(t):
    n=int(input())
    a=input()
    b=input()
    A,B,draw=0,0,0
    for i in range(n):
        if(a[i]=="R" and b[i]=="S"):
            A+=1
        elif(a[i]=="S" and b[i]=="R"):
            B+=1
        elif(a[i]=="S" and b[i]=="P"):
            A+=1
        elif(a[i]=="P" and b[i]=="S"):    
            B+=1
        elif(a[i]=="P" and b[i]=="R"): 
            A+=1
        elif(a[i]=="R" and b[i]=="P"):
            B+=1 
        elif(a[i]==b[i]):
            draw+=1    
    nonDraw=n-draw         
    if(A<B):
        print(((nonDraw//2)+1)-A) 
    else:
        print(0)          


            
