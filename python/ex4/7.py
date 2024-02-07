#gcd of 2 numbers
a = int(input("Enter num1:"))
b = int(input("Enter num2:"))
if(a<b):
	a,b=b,a
r = a%b
while(r!=0):
	a = b
	b = r
	r = a%b
print("GCD of the 2 numbers is", b)