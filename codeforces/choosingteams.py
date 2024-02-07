a=input().split()
n=int(a[0]) 
k=int(a[1])
y=input().split()
count=0
for  i in range(n):
    if(5-int(y[i])>=k):
        count+=1
print(count//3)        

