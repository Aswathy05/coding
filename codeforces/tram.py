n=int(input())
count=0
lst=[]
for i in range(n):
    x=input().split()
    a=int(x[0])      #in 
    b=int(x[1])       #out
    count-=a
    count+=b
    lst.append(count)
print(max(lst))    
  
    
    