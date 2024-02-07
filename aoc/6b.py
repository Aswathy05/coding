x=input().split()
x=x[1:]
time=""
for i in x:
    time+=i
time=int(time)    

y=input().split()
dist=""
y=y[1:]
for i in y:
    dist+=i 
dist=int(dist)

for i in range(time):
    if(i*(time-i)>(dist)):
        start=i
        end=time-i
        ways=end-start+1
        break
print(ways)    
        

    
    

