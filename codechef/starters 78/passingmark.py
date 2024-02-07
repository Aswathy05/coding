t=int(input())
for i in range(t):
    a=input()
    lst=a.split()
    n=int(lst[0])       #no of students in the class
    x=int(lst[1])       #no of students who passed
    mark=input()        #mark of respective students
    max=max(mark)
    print(max)
