n=int(input('Number of students : '))
d={}
d1={101:0,102:0,103:0}
for i in range(n):
    reg=input("Reg. No. : ")
    for i in d1:
        print("Enter subject-{} marks : ".format(i))
        cat1=int(input("CAT 1 : "))
        cat2=int(input("CAT 2 : "))
        sat=int(input("SAT : "))
        d1[i]=[cat1,cat2,sat]
    d[reg]=d1
#Display the information of a student given his register number
print("STUDENT DETAILS : ")
reg=input("Enter reg. no. : ")
for i in d[reg]:
    print("Subject-{} : ".format(i))
    print("CAT 1 :",d[reg][i][0])
    print("CAT 2 :",d[reg][i][1])
    print("SAT :",d[reg][i][2])
#To display the marks of a student given his subject code
print("STUDENT SUBJECT DETAILS : ")
reg=input("Enter reg. no. : ")
sub=int(input("Enter subject code : "))
print("Subject-",sub)
print("CAT 1 :",d[reg][sub][0])
print("CAT 2 :",d[reg][sub][1])
print("SAT :",d[reg][sub][2])
#Update the details of the student given the register number
print("UPDATE DETAILS : ")
reg=input("Enter reg. no. : ")
for i in d1:
        print("Enter subject-{} marks : ".format(i))
        cat1=int(input("CAT 1 : "))
        cat2=int(input("CAT 2 : "))
        sat=int(input("SAT : "))
        d1[i]=[cat1,cat2,sat]
d[reg]=d1
print(d)