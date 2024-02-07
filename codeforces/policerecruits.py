n=int(input())
lst=input().split()
lst1=[]
for i in lst:
    lst1.append(int(i))
count=0    
for i in lst1:
    if(i==-1):
        count+=-1
            