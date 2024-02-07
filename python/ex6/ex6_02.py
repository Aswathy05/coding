#program to print the prime digits of the given number
res = 0
def prime_finder(n):
	global res
	res = 0
	i=2
	if(n == 1):
		res = 1
	while(i*i<=n):
		if(n%i==0):
			res = 1
		i+=1

def separation():
	global res
	num = int(input("Enter the number:"))
	while(num>0):
		digit = num%10
		prime_finder(digit) 
		if(res==0):
			print("{} is a prime".format(digit))
		num //= 10

separation()
