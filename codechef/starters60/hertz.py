#Dog can hear in the range 67Hz to 45000Hz YES-if he can hear NO-if he cannot
T=int(input())
for i in range(T):
    X=int(input())
    if(X>=67 and X<=45000):
        print("YES")
    else:
        print("NO")    