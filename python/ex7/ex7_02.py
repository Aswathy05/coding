#program to generate 10 random numbers from 0 to 6 as a list and remove duplicates using a function

import random

def rem_dup(lst):
	temp = []
	for i in lst:
		if(i not in temp):
			temp.append(i)
	return temp
 	
lst=[]
for i in range(10):
	val = random.randint(0,6)
	lst.append(val)
print("Generated list:",lst)
lst = rem_dup(lst)
print("New list:",lst)
			
