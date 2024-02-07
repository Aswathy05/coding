#current worth-A billion dollars, increases X billion years every year, max worth B billion dollars
T=int(input())
for i in range(T):
    a=input()
    lst=a.split()
    A=int(lst[0])
    B=int(lst[1])
    X=int(lst[2])
    years=(B-A)//X
    print(years)