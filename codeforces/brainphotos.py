lst=input().split()
n=int(lst[0])
m=int(lst[1])
lst=[]
for i in range(n):
    row=input().split()
    lst.append(row)    
count=0    
for i in range(len(lst)):
    for j in lst[i]:
        if(j=="C" or j=="M" or j=="Y"):
            count+=1
            break
if(count!=0):         
    print("#Color")                
else:
    print("#Black&White")