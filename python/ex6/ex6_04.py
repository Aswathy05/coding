#create a function to display the factors of the given number. If the number is not given, use default value.

def facts(n=20):
	i=1
	while(i<=n):
		if (n%i==0):
			print(i) 
		i+=1

n = input("Enter a number:")
if n.isdecimal():
	facts(int(n))
else:
	facts()

