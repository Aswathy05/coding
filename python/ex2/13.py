a=int(input("Enter the coefficient of x^2:"))
b=int(input("Enter the coeffiecient of x:"))
c=int(input("Enter the constant:"))
d=(b**2-4*a*c)**0.5
x1=(-b+d)/2*a
x2=(-b-d)/2*a
print(x1,x2)