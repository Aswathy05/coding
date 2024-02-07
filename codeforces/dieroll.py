lst=input().split()
y=int(lst[0])
w=int(lst[1])
A=(6-(max(y,w)))
if(6%A!=0):
    print(A,"/",6)
else:
    print()    