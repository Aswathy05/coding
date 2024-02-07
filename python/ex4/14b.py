#print the sum of the series -----  -x + x^2 – x^3 + x^4+....
x = int(input("Enter x:"))
n = int(input("Enter n:"))
sum = 0
for i in range(1,n+1):
	if(i%2==1):
		print("-",x,"^",i,sep="",end=" ")
		sum -= x**i
	else:
		print("+",x,"^",i,sep="",end=" ")
		sum += x**i
	
print("=",sum)