#get list of names from user. find how many times "a" appear in the list

n = int(input("Enter number of names:"))
lst = [x for x in input("Enter the names:").split()]
count=0
for i in lst:
	for j in i:
		if(j=="a"):
			count+=1
print("a appears {} times".format(count))
