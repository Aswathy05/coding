t=int(input())
for j in range(t):
    n=int(input())
    count=0
    while(n!=50):
        if(n>50):
            n-=3
            count+=1 
        elif(n<50):
            n+=2
            count+=1
    print(count)        