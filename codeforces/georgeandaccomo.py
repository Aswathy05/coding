n=int(input())
count=0
for i in range(n):
    x=input()
    lst=x.split()
    p=int(lst[0])     #no of people living in the room  
    q=int(lst[1])     #room's capacity
    if((q-p)>=2):
        count+=1
print(count)           