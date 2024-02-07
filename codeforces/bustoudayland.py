t=int(input())
out=[]
lst=[]
for i in range(t):
    a=input()
    out.append(a)
    lst.append(a.split("|"))
count=0    
for i in range(t):
    for j in range(2):
        if(lst[i][j]=="OO"):
            i1=i
            j1=j 
            count+=1
            break
    if(count==1):
        break
if(count==0):
    print("NO")
else: 
    print("YES")   
    for i in range(t):
        if(i==i1 and j1==0):
            print("++","|",lst[i][1],sep="")     
        elif(i==i1 and j1==1):
            print(lst[i][0],"|","++",sep="")        
        else:
            print(lst[i][0],"|",lst[i][1],sep="")    