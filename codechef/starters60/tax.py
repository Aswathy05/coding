#if income is >100 reduce 10 from the income else same income
T=int(input())
for i in range(T):
    x=int(input())
    if(x>100):
        print(x-10)
    else:
        print(x)    