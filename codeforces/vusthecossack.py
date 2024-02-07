lst=input().split()
n=int(lst[0])
m=int(lst[1])
k=int(lst[2])
if(min(m,k)<n):
    print("no")
else:
    print("yes")    