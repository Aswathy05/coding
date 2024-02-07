# to print the sequence --- 1,3,9,27,81,243...
n = int(input("Enter number of terms:"))
x=1
for i in range(n):
    if(i!=n-1):
        print(x,end=",") 
    else:
        print(x)
    x*=3	