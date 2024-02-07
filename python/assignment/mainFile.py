import Student
import Testschedule

print("Welcome to Test Management System")

while(True):

    addedit = int(input("Use 1 to add new data to the Student repository. Use 2 to edit the student repository: "))

    if(addedit == 1):
        student_register_num, student_dict = Student.getStudentDetails()
        