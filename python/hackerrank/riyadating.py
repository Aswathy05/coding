x=input()
lst=x.split()
a=int(lst[0])
d=int(lst[1])
N=int(lst[2])
n1=(N-(a+d))/d
n2=(N-(a+d))//d
if(n1==n2):
    print("1")
else:
    print("0")