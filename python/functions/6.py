def factorial():
    if(n<1):
        return 1
    else:
        return n*factorial(n-1)    

n=int(input("Enter a number:"))
fact=factorial(n)
print(fact)