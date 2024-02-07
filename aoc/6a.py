x=input().split()
x=x[1:]
time=[]
for i in x:
    time.append(int(i))
y=input().split()
y=y[1:]
dist=[]
for i in y:
    dist.append(int(i))    
pdt=1
for z in range(len(time)):    
    for i in range(time[z]):
        if(i*(time[z]-i)>(dist[z])):
            start=i
            end=time[z]-i
            ways=end-start+1
            pdt=pdt*ways        
            break
print(pdt)             

    
    

