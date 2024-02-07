#check whether given number is palindrome or not
n = int(input("Enter a number:"))
rev=0
temp=n
while(n>0):
	rev = (rev*10)+(n%10)
	n//=10
print(rev)
if(rev==temp):
	print("It is a palindrome")
else:	
	print("It is not a palindrome")
