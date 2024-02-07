#check whether a number is armstrong number or not
n = int(input("Enter a number:"))
sum=0
temp=n
while(n>0):
	digit=n%10
	sum+=(digit**3)
	n//=10
if(sum==temp):
	print("It is an armstrong number")
else:
	print("It is not an armstrong number")