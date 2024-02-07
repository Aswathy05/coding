import sys
sys.stdin=open("input.txt","r")
sys.stdout=open("output.txt","w")
n,m=(int(i) for i in input().split())
a=input().split()
for i in range(n):
    a[i]=int(a[i])
 
a.sort() 
sum=0
for i in range(m):
    if(a[i]<=0):
        sum+=(-1*(a[i]))
print(sum)
   
         
