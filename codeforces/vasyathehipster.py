x=input()
lst=x.split()
a=int(lst[0])       
b=int(lst[1]) 
if(a<b):
    a,b=b,a
lst1=[]    
lst1.append(b)
a=a-b
lst1.append(a//2) 
for i in lst1:
    print(i,end=" ")   


