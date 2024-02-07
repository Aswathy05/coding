#print the sum of the series ----- 1 + x^2/2 + x^3/3 + ... x^n/n
x = int(input("Enter x:"))
n = int(input("Enter n:"))
sum = 1
print(1,"+",sep="",end="")
for i in range(2,n+1):
	print(x,"^",i,"/",i,"+",sep="",end="") if(i!=n) else print(x,"^",i,"/",i,sep="",end="")
	sum += ((x**i)/i)
print("=",sum)                                                                     
