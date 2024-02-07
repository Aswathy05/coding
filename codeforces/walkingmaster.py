t=int(input())
for i in range(t):
    x=input()
    lst=x.split()
    a=int(lst[0])       
    b=int(lst[1]) 
    c=int(lst[2])
    d=int(lst[3])  
    while a==c or b==d:
        a+=1
        b+=1
        print(a,b)    
