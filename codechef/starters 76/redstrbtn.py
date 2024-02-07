'''111
112
113
221
'''
T=int(input())
for i in range(T):
    a=input()
    lst=a.split()
    x=int(lst[0])
    y=int(lst[1])
    z=int(lst[2])
    if(x==1 and y==1 and z==1):
        print("no")
    elif(x==1 and y==1 and z==2):
        print("no") 
    elif(x==1 and y==2 and z==1):
        print("no")    
    elif(x==2 and y==1 and z==1):
        print("no")        
    elif(x==1 and y==1 and z==3):
        print("no")
    elif(x==1 and y==3 and z==1):
        print("no")    
    elif(x==3 and y==1 and z==1):
        print("no")    
    elif(x==2 and y==2 and z==1):
        print("no")    
    elif(x==1 and y==2 and z==2):
        print("no")   
    elif(x==2 and y==1 and z==2):
        print("no")           
    else:
        print("yes")       
