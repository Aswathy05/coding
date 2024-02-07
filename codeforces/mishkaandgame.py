n=int(input())
m1,c1,eq=0,0,0
for i in range(n):
    lst=input().split()
    m=lst[0]
    c=lst[1]
    if(m>c):
        m1+=1
    elif(c>m):
        c1+=1   
if(m1>c1):
    print("Mishka")            
elif(c1>m1):
    print("Chris")
else:
    print("Friendship is magic!^^")