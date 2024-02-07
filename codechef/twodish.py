T=int(input())
for i in range(T):
    a=input()
    lst=a.split()
    N=int(lst[0])   #total dishes
    A=int(lst[1])   #fruits
    B=int(lst[2])   #vegetable
    C=int(lst[3])   #fishes
    if(A=B and B=N):
        print("YES")    