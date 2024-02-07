#finding the roots of a given quadratic equation
a= int(input("Coeff of x^2:"))
b = int(input("Coeff of x:"))
c= int(input("Constant"))
disc = (b**2)-(4*a*c)
if(disc>0):
    print("Real and Distinct roots")
elif(disc==0):
    print("Real and Equal roots")
else:
    print("Imaginary roots")
r1 = ((-1*b)+(((b*b)-4*a*c))**0.5)/(2*a)
r2 = ((-1*b)-(((b*b)-4*a*c))**0.5)/(2*a)
print(r1, r2)