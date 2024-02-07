#create a list of students name and do the linear and binary search
student_name=[]
n=int(input("Enter no.of students:"))
for i in range(n):
    name=input("Enter student name:")
    student_name.append(name)
print("Students name:",student_name)
key_name=input("Enter a student name:")
def linear(key,lst):
    for j in range(len(lst)):
        if lst[j]==key_name :
            return j
    else :
        return -1
lin_search=linear(key_name,student_name)
print("Using linear search")
if lin_search==-1:
    print("Student name not found")
else :
    print("Name found at",lin_search)
def sort(lst):
    for i in range(len(lst)):
        for j in range(0,len(lst)-i-1):
            if lst[j]>lst[j+1]:
                lst[j],lst[j+1]=lst[j+1],lst[j]
    return lst
bub_sort=sort(student_name)
print("Sorted name list:",bub_sort)
def binary(key,lst,low,high):
    if high >= low :
        mid=low+(high-low)//2
        if lst[mid]==key:
            return mid
        elif lst[mid]>key:
            return binary(key,lst,low,mid-1)
        else:
            return binary(key,lst,mid+1,high)
    else:
        return -1
low=0
high=len(bub_sort)-1
key_name1=input("Enter a student name:")
bin_search=binary(key_name1,bub_sort,low,high)
print("Using binary search")
if bin_search==-1 :
    print("Name not found")
else:
    print("Name found at",bin_search)


 
