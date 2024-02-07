#fibo series with recursive functions\
#0 1 1 2 3 5 8 13 21 
def Fibo(x):
    if x<=1:
        return x
    else:
        return Fibo(x-1) + Fibo(x-2)
x=int(input("Enter no of terms:"))
if x>0:
    for i in range(x):
        print(Fibo(i))
else:
    print("Invalid Input")
    