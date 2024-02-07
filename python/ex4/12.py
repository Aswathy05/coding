#find the factorial of a given number
num = int(input("Enter the number:"))
res = 1
for i in range(1,num+1):
	res*=i
print("Factorial of {} is {}".format(num,res))