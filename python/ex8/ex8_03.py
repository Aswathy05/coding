mark_list=[('Rams',120,55,45,65,45,32),('Vel',121,94,86,78,67,90),('Siri',122,73,98,90,87,89)]
lst=[]
for i in mark_list:
    tup=()
    for j in range(len(i)):
        if j==0:
            tup+=(i[0],)
        elif j ==1:
            tup+=(i[1],)
        else:
            if i[j]>=90:
                tup+=("grade A",)
            elif i[j]>=80:
                tup+=("grade B",)
            elif i[j]>65:
                tup+=("grade C",)
            elif i[j]>=40:
                tup+=("grade D",)
    lst.append(tup)
print(lst)