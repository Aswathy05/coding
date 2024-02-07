d={"Achu":(9.8,9.7),"Pradeep":(9.5,9.9),"Abish":(9.8,9.6),"Shaun":(9.5,9.0),"Aashi":(9.9,9.8)}
def CGPA_stud():
    add=0
    gpa=d.values()
    for i in gpa:
        for j in i:
            add+=j
        cgpa=(add)/2
        print(cgpa)
    return cgpa
print(CGPA_stud())    
