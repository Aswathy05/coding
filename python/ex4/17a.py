#program to print the pattern
'''
1
2 1
3 2 1
4 3 2 1 

'''

for i in range(1,5): 
	for j in range(i,0,-1):
		print(j,end=" ")
	print()
