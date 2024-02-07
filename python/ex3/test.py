ch=int(input("Enter a number:"))
vow=[1,2,3,4,5]
res=0
for i in vow:
    if(i==ch):
        res=1
if(res==1):
    print(ch,"is in the box")
else:
    print(ch,"is not in the box")