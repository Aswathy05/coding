d={'Niranjan':(9.8,9.0),'Nithish':(8.8,9.3),'Bharathi':(7.6,8.4),'Yhokesh':(9.9,9.7),'Titus':(9.1,9.0)}
def CGPA_stud():
    global d
    for i in d:
        d[i]=(d[i][0]+d[i][1])/2
def display_names():
    global d
    names=d.keys()
    names=list(names)
    names.sort()
    d1={}
    for i in names:
        d1[i]=d[i]
    return d1 
def display_grade():
    global d
    cgpa=d.values()
    cgpa=list(cgpa)
    cgpa.sort()
    d1={}
    for i in cgpa[::-1]:
        for j in d:
            if i==d[j]:
                d1[j]=i
    return d1
CGPA_stud()
print("CGPA of students :",d)
d1=display_names()
print("CGPA list in ascending order of names :")
print(d1)
d1=display_grade()
print("CGPA list in descending order of grades :")
print(d1)