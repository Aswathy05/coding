def happysad(num):
	res= 0 
	lst = list()
	temp = num
	print("{} =".format(num),end="")
	while(num>0):
		digit = num%10
		res += (digit**2)
		num//=10
		lst.append(digit)
		print("{}**2 + ".format(digit),end="") if num>0 else print("{}**2 = ".format(digit),end="")
	for i in range(len(lst)):
		print("{} + ".format(lst[i]**2),end="") if(i!=len(lst)-1) else print("{} = ".format(lst[i]**2),end="")
	print(res)
	if(res==1):
		print(n, "is a happy number")
	elif(res%10 == res):
		print(n, "is a sad number")
	else:
		happysad(res)

n =int(input("Enter the number:"))
happysad(n)



