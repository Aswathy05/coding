#square root using newton's method
n = int(input("Enter a number:"))
temp = n
while(1):
	root = (n+(temp/n))/2
	if(n==root):
		break
	n = root
print("Square root is",root)