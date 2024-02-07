x=input()
lst=x.split()
n=int(lst[0])       #number 
k=int(lst[1])       #no of subtrations
for i in range(k):
    l=n%10
    if(l==0):
        n=n//10
    else:
        n=n-1    
print(n)   

