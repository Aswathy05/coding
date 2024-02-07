def primelst(num):
    res=0
    i = 2
    lst1=[2]
    while(i<num):
        if(num%i==0):
            res=1
            break
        i+=1
    if(res!=1):
        lst1.append(i)
    return lst1
def prime(num):
    res=0
    i = 2
    while(i<num):
        if(num%i==0):
            res=1
            break
        i+=1
    if(res!=1):
        return primelst(num)
lst=input().split()
num1=int(lst[0])
num=int(lst[1])
print(prime(num))
