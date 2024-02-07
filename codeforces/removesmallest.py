t=int(input())
for j in range(t):
    n=int(input())
    x=input().split()
    lst=[]
    for i in x:
        lst.append(int(i))
    lst1=sorted(lst)    
    count=0    
    for i in range(len(lst1)-1):
        if((lst1[i+1]-lst1[i])>1):
            print("no")
            count+=1
            break
    if(count!=1):
        print("yes")    


        

            
            