#generate the sum of odd numbers and even numbers in the range of N numbers

def oddeven(n):
	oddsum = 0
	evensum = 0
	for i in range(1,n+1):
		if(i%2==0):
			evensum += i
		else:
			oddsum += i
	return (evensum, oddsum)

num = int(input("Enter the number:"))
even, odd = oddeven(num)
print("Sum of odd numbers till {} is {}".format(num,odd))
print("Sum of even numbers till {} is {}".format(num,even))
