t=int(input())
for i in range(t):
    lst=[]
    for i in range(3):
        s=input()
        lst.append(s)
    
    lst1=[]
    for i in range(3):
        count=0
        for j in range(3):
            if(lst[i][j]!="?"):
                count+=1
                
        if(count==2):
            lst1.extend((lst[i][0],lst[i][1],lst[i][2]))
            break
    if("A" not in lst1):
        print("A") 
    elif("B" not in lst1):
        print("B") 
    elif("C" not in lst1):
        print("C") 

                
                