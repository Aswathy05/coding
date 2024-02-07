n=int(input())
s=input()
z,n=0,0
for i in s:
    if(i=="z"):
        z+=1
    elif(i=="n"):
        n+=1  
lst=[]
for i in range(n):
    lst.append(1)     
for i in range(z):
    lst.append(0)    
for i in lst:
    print(i,end=" ")          



