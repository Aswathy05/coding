def harshadnum(n):
	temp = n
	digitsum = 0
	while(temp>0):
		digit = temp%10
		digitsum+=digit
		temp//=10
	if(n%digitsum==0):
		print("{} is a Harshad number".format(n))
	else:
		print("{} is not a Harshad number".format(n))

num = int(input("Enter a number:"))
harshadnum(num)

