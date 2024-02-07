t=int(input())
for i in range(t):
    s=input()
    a,b,c=0,0,0
    for j in s:
        if(j=="A"):
            a+=1
        elif(j=="B"):
            b+=1
        elif(j=="C"):
            c+=1
    if(a==c and b==0):
        print("no")    
    elif(a+b==c or a+c==b):
        print("yes")      
    else:
        print("no")    