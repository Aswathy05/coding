n=int(input())
lst=[]
for i in range(n):
    x=input()
    lst.append(x)
lst1=[] 
s=""   
for i in lst[::-1]:
    if(i not in lst1):
        lst1.append(i)        
        s+=i[len(i)-2:]
print(s)     