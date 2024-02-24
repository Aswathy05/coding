t=int(input())
for i in range(t):
    n=int(input())
    lst=[1,2,4,8,16,32,64]
    tot=sum(lst)
    if(n>=tot):
        print("yes")
    else:
        print("no")    