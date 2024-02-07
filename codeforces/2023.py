t=int(input())
for i in range(t):
    n,a=(int(i) for i in input().split())
    b=input().split()
    b1=[]
    for i in b:
        b1.append(int(i))
    pdt=1
    for i in b1:
        pdt=pdt*i    
     
    if(2023%pdt==0 and a>1):
        print("yes")
    else:
        print("no")
