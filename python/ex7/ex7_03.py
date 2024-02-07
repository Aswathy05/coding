#Create a list arr with “n” integers, construct a new list prod_list of same size such that prod_list[i] is equal to the product of all the elements of arr except arr[i].

def prod(lst,i):
	ans = 1
	for j in lst[:i]+lst[i+1:]:
		ans*=j
	return ans
n = int(input("Enter number of elements:"))
lst=[]
for i in range(n):
	val = int(input("Enter value{}:".format(i+1)))
	lst.append(val)

prod_lst=[]

for i in range(len(lst)):
	product = prod(lst,i)
	prod_lst.append(product)
print("Product list:",prod_lst)



