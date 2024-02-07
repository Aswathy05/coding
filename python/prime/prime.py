num = int(input())
res=0
i = 2
while(i<num):
    if(num%i==0):
        res=1
        break
    i+=1
if(res==1):
    print("Not a prime")
else:
    print("Prime")