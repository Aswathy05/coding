t=int(input())
for i in range(t):
    n=int(input())
    s=input().split()
    x=[]
    for i in s:
        x.append(int(i))
    dict={} 
    time=[]
    for z in range(1,n+1):
        
        timecount=0
        lst1=x.copy() 
        lst=x.copy()  
        if(z not in lst):
            continue
        while(len(set(lst))>1):
            print(timecount)
            for i in range(n):
                print(lst1)
                if(len(set(lst))==1):
                    break
                elif(i==0 and lst[i]==z and lst[i+1]!=z):
                    lst1[i+1]=z

                elif(i==0 and lst[i]==z and lst[i+1]==z):
                    continue
                elif(i==0 and lst[i]!=z):
                    lst[i]=z
                    
                elif(i==(n-1) and lst[i]==z and lst[i-1]!=z):
                    lst1[i-1]=z
                elif(i==(n-1) and lst[i]==z and lst[i-1]==z):
                    continue
                elif(i==(n-1) and lst[i]!=z):
                    if(x[n-2]==z):
                        lst1[i]=z
                        print(lst,"aioo")
                    else:
                        count=0
                        for i in range(len(lst)-1):
                            if(lst[i]!=z):
                                count+=1
                        if(count==0):
                            lst1[i]=z
                            timecount+=1
                            
                            break      
                        else:
                            break
                elif(lst[i]==z and lst[i+1]!=z and lst[i-1]!=z):
                    lst1[i+1]=z
                    lst1[i-1]=z

                elif(lst[i]==z and lst[i+1]!=z):
                    lst1[i+1]=z
                    if(lst[i-1]!=z):
                        lst1[i-1]=z

                elif(lst[i]==z and lst[i-1]!=z):
                    lst1[i-1]=z
                    if(lst[i+1]!=z):
                        lst1[i+1]=z
            lst=lst1            
            timecount+=1

        dict[z]=timecount 
        minClan = min(dict, key=dict.get)
        minDays = min(dict.values(), key=lambda x: x)
    print(minClan,minDays)
                

