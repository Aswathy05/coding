#exponentiation without ** operator
base = int(input("Enter the base:"))
exp = int(input("Enter the exponent:"))
res=1
while(exp!=0):
	res*=base
	exp-=1
print("The answer is",res)