n=int(input())
sum=0
lst=[]
while(True):
    sum+=2
    lst.append(2)
    if(sum<n):
        break

if(n%2==0):    
    lst.append(2)    
else:
    lst.append(3)
print(len(lst))    
for i in lst:
    print(i,end=" ")    