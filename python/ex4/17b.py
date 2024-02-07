#program to print the following pattern
'''
    *
   * *
  * * *
 * * * *
* * * * *

'''
for i in range(5):
	print(" "*(5-i-1),end="")
	for j in range(i+1):
		print("*",end=" ")
	print()