# list of n students cleared jee. list of m students cleared neet. both exams. only jee. only neet. atleast 1 exam

jee = ["a","b","c","d","e"]
neet = ["c","d","e","f","g"]

#cleared both
print("Students who cleared Both exam:")
for i in jee:
	if i in neet:
		print(i)

#only jee
print("Students who cleared only JEE exam:")
for i in jee:
	if i not in neet:
		print(i)

#only neet
print("Students who cleared only NEET exam:")
for i in neet:
	if i not in jee:
		print(i)

#atleast 1 exam
print("Students who cleared atleast 1 exam:")
lst = []
for i in jee+neet:	
	if i not in lst:
		lst.append(i) 
for i in lst:
	print(i)
