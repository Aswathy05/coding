t=int(input())
for i in range(t):
    x=int(input())
    if(x%10<5):
        print(100-(x-x%10))
    else:
        print(100-(x+(10-x%10)))