#display the results based on percentage of marks
m1 = int(input("Enter Mark1:"))
m2 = int(input("Enter Mark2:"))
m3 = int(input("Enter Mark3:"))
m4 = int(input("Enter Mark4:"))
m5 = int(input("Enter Mark5:"))
tot = m1+m2+m3+m4+m5
per = tot/500*100
if(per>=90):
    print("Distinction")
elif(per>=80 and per<90):
    print("First Class")
elif(per>=70 and per<80):
    print("Second Class")
elif(per>=60 and per<70):
    print("Third Class")
else:
    print("Fail")

