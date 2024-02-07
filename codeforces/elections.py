t=int(input())
for i in range(t):
    lst=input().split()
    a=int(lst[0])
    b=int(lst[1])
    c=int(lst[2])
    maxi=(max(a,b,c))
    lst1=[]
    if(a==0 and b==0 and c==0):
        print(1,1,1)
    else:    
        if(a!=maxi):
            lst1.append(maxi+1-a)
        else:
            lst1.append(0)    
        if(b!=maxi):
            lst1.append(maxi+1-b)
        else:
            lst1.append(0)     
        if(c!=maxi):
            lst1.append(maxi+1-c)
        else:
            lst1.append(0)     
        for j in lst1:
            print(j, end=" ")   
        print()