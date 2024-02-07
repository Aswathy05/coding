t=int(input())
for i in range(t):
    n=int(input())
    s=input()
    one,zero=0,0
    for i in s:
        if(int(i)==1):
            one+=1
        else:
            zero+=1  
    print(zero,one)        
    if(one>1 and zero>1 and one%2==0 and zero%2==0):
        print("no")  
    elif(one>1 and zero>1 and one%2!=0 and zero%2==0):  
        print("no") 
    elif(one>1 and zero>1 and one%2==0 and zero%2!=0):    
        print("no")    
    elif(n>1 and one==0 and zero!=0):
        print("no")    
    elif(n>1 and one!=0 and zero==0):
        print("no")    
    else:
        print("yes")    