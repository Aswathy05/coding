#displaying the grade of the student based on the average of marks obtained
a= int(input("Enter subject1 mark:"))
b=int(input("Enter subject2 mark:"))
c=int(input("Enter subject3 mark:"))
avg = (a+b+c)/3
if(avg>=90 and avg<=100):
    print("Grade:A")
elif(avg>=80 and avg<=89):
    print("Grade:B")
elif(avg>=70 and avg<=79):
    print("Grade:C")
elif(avg>=60 and avg<=69):
    print("Grade:D")
else:
    print("Grade:F")
