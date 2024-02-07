t=int(input())
for i in range(t):
    n=int(input())
    s1=input()
    s2=input()
    lst1=[]
    for j in s1:
        if(j=="G"):
            lst1.append("B")
        else:
            lst1.append(j)  
    lst2=[]        
    for j in s2:
        if(j=="G"):
            lst2.append("B")
        else:
            lst2.append(j) 
    if(lst1==lst2):
        print("yes")                  
    else:
        print("no")	