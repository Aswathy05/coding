x=input()
lst=x.split()
k=int(lst[0])       #cost of 1st banana
n=int(lst[1])       #initial number of money he has
w=int(lst[2])       #no of bananas he wants
amt=0
for i in range(w+1):
    amt+=i*k
    i=i+1
if(amt<=n):
    print(0)
else:
    print(amt-n)    