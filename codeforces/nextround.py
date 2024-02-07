x=input()
lst=x.split()
n=int(lst[0])       #number of participants
k=int(lst[1])       #score should be equal or greater than this kth place contestant
lst1 = [int(x) for x in input().split()]
count=0
for i in lst1:
    if(i<=0):
        count+=0 
    elif(i>=lst1[k-1]):
        count+=1       
print(count)        