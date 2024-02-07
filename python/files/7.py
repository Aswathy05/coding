def sort_studentname(file_name):
    with open(file_name,"r") as f:
        names = f.read().split()
        names.sort()
        print(names)
sort_studentname("student.txt")        