#odd+odd=even 
#odd+even=odd
#even+even=even
t=int(input())
for i in range(t):
    n=int(input())
    a=input().split()
    a1=[]
    for j in a:
        a1.append(int(j))
    even,odd=[],[]
    for j in a1:
        if(j%2==0):
            even.append(j)  
        else:
            odd.append(j)
    if(len(even)==len(odd)):
        print("yes")              
    else:
        print("no")    