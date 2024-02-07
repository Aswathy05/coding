#program to print the sequence ---- 1,8,27,64..

n = int(input("Enter the number of terms:"))
for i in range(1,n+1):
	print(i**3,end=",") if(i!=n) else print(i**3)
