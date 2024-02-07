#program to print numbers from 0 to 7 except 3 and 6. Use continue statement
for i in range(8):
	if(i==3 or i==6):
		continue
	print(i,end=" ")