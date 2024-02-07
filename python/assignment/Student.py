student_dict = {}
student_rep_dict = {}

def getStudentDetails():
    global student_dict
    student_name = input("Enter name of the student:")
    register_num = int(input("Enter the register number of the student:"))
    mail_id = input("Enter the student's Mail id:")
    student_section = input("Enter the student's section:")
    student_dict[register_num] = [student_name, student_section, mail_id]
    return register_num, student_dict

'''def addStudentToRepos(student_section, register_num):'''

