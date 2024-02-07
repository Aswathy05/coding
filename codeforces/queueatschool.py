a=input().split()
n=int(a[0])
t=int(a[1])
lst=list(input())
while(t>0):
    t-=1
    i=0
    lst1=[]
    while(i<len(lst)):
        if(i<len(lst)-1 and lst[i]=="B" and lst[i+1]=="G"):
            lst1.extend([lst[i+1], lst[i]])
            i+=2
        else:
            lst1.append(lst[i])
            i+=1
    lst = lst1
for i in lst:
    print(i, end="")
    