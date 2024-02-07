def assign_grade(lst):
    if(marks>=90):
        print("A")
    elif(marks>=80 and marks<90):
        print("B")    
    elif(marks>=65 and marks<80):
        print("C")    
    elif(marks>=40 and marks<60):
        print("D")
    elif(marks<40):
        print("F")      
lst=[]          
for i in range(5):
    marks=int(input("Enter marks:"))  
    lst.append(marks)    
    assign_grade(marks)
print(lst)    