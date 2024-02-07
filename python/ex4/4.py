D=int(input("Enter the dividend:"))
d=int(input("Enter the divisor:"))
x=D
n=0
while(x>=d):
    x-=d
    n+=1
print("The quotient is",n) 
print("The remainder is",x)
   