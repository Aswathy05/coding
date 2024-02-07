#finding the type of triangle with sides
a=int(input("Enter side1:"))
b=int(input("Enterside2:"))
c=int(input("Enter side3:"))
if(a==b and b==c):
    print("The triangle is Equilateral")
elif(a==b or a==c or b==c):
    print("The triangle is Isosceles")
else:
    print("The triangle is Scalene")

