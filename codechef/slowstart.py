t=int(input())
for i in range(t):
    lst=input().split()
    x=int(lst[0])
    h=int(lst[1])
    count=0
    
    while(count<5):
        h-=x/2
        count+=1
        if(h<=0):
            print(count)
            break
       
    if(count==5 and h>0):
        if(h%x==0):
            count+=h//x
        else:
            count+=((h//x)+1)
        print(int(count))

