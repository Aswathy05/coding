t=int(input())
for i in range(t):
    n=int(input())
    lst1=input().split()
    lst2=input().split()
    lst3=[]
    count=0
    for i in range(n):
        count+=1
        if(lst1[i]=="0" and i<n):
            lst3.append(count-1)  
            count=0
        elif(i==n-1):
            lst3.append(count)   
    lst4=[]    
    count=0
    for i in range(n):
        count+=1
        if(lst2[i]=="0" and i<n):
            lst4.append(count-1)  
            count=0
        elif(i==n-1):
            lst4.append(count)                   
    Om=max(lst3)
    Addy=max(lst4)        
    if(Om>Addy):
        print("Om")
    elif(Addy>Om):
        print("Addy")   
    else:
        print("Draw")     