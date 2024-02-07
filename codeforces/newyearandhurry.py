#4hrs= 4*60 = 240 mins
x=input()
lst=x.split()
n=int(lst[0])      
k=int(lst[1]) 
t=240-k     
time,count=0,0
for i in range(1,n+1): 
    time=i*5       
    t=t-time        
    if(t<0):
        break
    count+=1       
print(count)            