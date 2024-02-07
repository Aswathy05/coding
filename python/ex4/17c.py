#program to print the following pattern
"""
            1
          1   1
        1   2   1
      1   3   3   1
    1   4   6   4   1
  1   5   10  10  5   1
1   6   15  20  15  6   1

"""
from math import factorial
n = 7
for i in range(n):
	for j in range(n-i+1):
		print(end="  ")
	for j in range(i+1):
		res = factorial(i)//(factorial(j)*factorial(i-j))
		tempres=res
		count = 0
		while(tempres>0):
			count+=1
			tempres=tempres//10
		if(count==2):
			print(res,"  ",sep="",end="")
		elif(count==1):
			print(res,"   ",sep="",end="")
	print()