#perform operations with the list data

data=[5,3,7]

#negating 0th index element
data[0]=-data[0]
print("List after negating 0th index element:", data)

#adding 10 to the end
data.append(10)
print("List after adding 10 to data in the end:", data)

#inserting 22 at 2nd index
data.insert(2, 22)
print("List after inserting 22 at index 2:", data)

#remove element at index 1
del data[1]
print("List after removing value at index 1:", data)

#add elements of newData to the end of Data
newData = [9,11,13]
data+=newData
print("List after adding newData to the end:", data)

#locate the element 7
for i in range(len(data)):
	if(data[i]==7):
		print("7 is located at", i)

#find the maximum of the list
maxi = data[0]
for i in data:
	if(i > maxi):
		maxi = i
print("Maximum value:", maxi)

#finding the sum of elements of the list
sum = 0
for i in data:
	sum+=i
print("Sum of elements in data:", sum)

#sorting the list
print("The sorted list is", sorted(data))


