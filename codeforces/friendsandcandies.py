t=int(input())
for j in range(t):
    n=int(input())
    a=input().split()
    lst=[]
    for i in a:
        lst.append(int(i))    
    max1=max(lst)  
    lst1=[] 
    for i in lst:
        lst1.append(max1-i) 
    lst.remove(max(lst))
    max2=max(lst)
    if(max2>=n):
        count=0
        for i in lst:
            count+=(max1-i)        
    else:
        lst.remove(max2)     
        maxi=max1+max2
        count=0
        for i in lst:
            count+=maxi-i   
    print(lst1,count)