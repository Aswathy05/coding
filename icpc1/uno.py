t=int(input())
for i in range(t):
    n,k=(int(i) for i in input().split())
    s=input()
    count=1
    r=0
    for i in s:
        if(r%2==0):
            if(i=="U"):
                if(count==n):
                    count=1
                else:
                    count+=1
            elif(i=="S"):
                if(count==n):
                    count=2
                elif(count==n-1):
                    count=1  
                else:
                    count+=2
            elif(i=="R"):
                r+=1
                if(count==1):
                    count=n
                else:    
                    count-=1  
        elif(r%2!=0):
            if(i=="U"):
                if(count==1):
                    count=n
                else:
                    count-=1
            elif(i=="S"):
                if(count==1):
                    count=n-1
                if(count==2):
                    count=n    
                else:
                    count-=2
            elif(i=="R"):
                r+=1
                if(count==n):
                    count=1
                else:    
                    count+=1          

    print(count)
