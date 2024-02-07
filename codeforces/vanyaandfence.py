x=input()
lst=x.split()
n=int(lst[0])       
h=int(lst[1])   
count=0 
x=input().split()
for i in x:
    if(int(i)<=h):
        count+=1
    else:
        count+=2
print(count)                