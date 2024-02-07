#program to swap two numbers using simultaneous assignment
a=int(input("Enter a value for a:"))
b=int(input("Enter a value for b:"))
a,b=b,a
print("The value of a after swapping=",a)
print("The value of b after swapping=",b)