#program to define a function and assign grades for the marks passed to the function as a list

def Assign_grade(lst):
	for i in range(len(lst)):
		mark = lst[i]
		if(mark>=90):
			grade="A"
		elif(mark>=80 and mark<90):
			grade="B"
		elif(mark>=65 and mark<80):
			grade="C"
		elif(mark>=40 and mark<65):
			grade="D"
		else:
			grade="F"
		print("Student{} grade is {}".format(i+1,grade))
lst = []
for i in range(5):
	val = int(input("Enter mark of Student{}:".format(i+1)))
	lst.append(val)
Assign_grade(lst)
print(lst)
