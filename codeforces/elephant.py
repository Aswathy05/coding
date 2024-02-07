x=int(input())      #12
lst=[5,4,3,2,1]
count=0
for i in lst:       #5
    q=x//i          #q=12//5=2
    r=x%i           #r=12%5=2
    count+=q        #count=0+q=q
    x-=q*i     
    if(r==0):
        break
print(count)        
        