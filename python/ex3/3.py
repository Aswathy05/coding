#finding the smallest of 3 numbers
a=int(input("Enter value1:"))
b=int(input("Enter value2:"))
c=int(input("Enter value3:"))
if (a<b and a<c):
    print(a, "is the smallest")
elif (b<c):
    print(b, "is the smallest")
else:
    print(c, "is the smallest")
