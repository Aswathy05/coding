#names of 10 students as a list. print. search for a particular student (linear search). Sort and search for a particular student(Binary search)

#binary search function
def bin(lst,high,low, x):
	for i in range(len(lst)):
		midind = low+((high-low)//2)
		mid = lst[midind]
		if(mid==x):
			return midind
		elif(b<mid):
			return bin(lst, midind-1, low, x)
		elif(b>mid):
			return bin(lst, high, midind+1, x)

#printing list
lst = [x for x in input("Enter the list of names:").split()]
print("The list is:",lst)

#linear search
a = input("Enter the name to find(Lin search):")
for i in range(len(lst)):
	if(lst[i]==a):
		print(a,"is found at index",i)
b = input("Enter the name to find(Bin search):")
lst.sort()
print("Sorted list:",lst)

#binary search
high = len(lst)-1
low = 0
ind = bin(lst, high, low, b)
print(b, "is found at", ind)


