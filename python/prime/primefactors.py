lst = []
num = int(input())
i=1
while(i*i<=num):
    if(num%i==0):
        lst.append(i)
        lst.append(int(num/i))
    i+=1
fac=[]  
for i in lst:
    res=0 
    j=2
    while(j**2<=i):
        if(i%j==0):
            res=1
            break
        j+=1
    if(res!=1):
        fac.append(i)
print(fac)