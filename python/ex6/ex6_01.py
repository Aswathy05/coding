#program to define the function that sums the digits of the input

def sum_of_digits(n):
	sum=0
	while(n>0):
		digit = n%10
		sum+=digit
		n//=10
	return sum

n = int(input("Enter the number:"))
sum = sum_of_digits(n)
print("Sum of digits = {}".format(sum))
