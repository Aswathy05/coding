x=int(input())
num=0
count=0
i=1
while(i<x):
    print(i)
    i+=((i*(i+1))//2)
    if(i==x):
        print(count)
    elif(i>x):
        break
    count+=1    
print(count+1)    

