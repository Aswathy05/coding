#program to display electricity bill based on number of units of power consumed
aunits= int(input("Enter previous month readings:"))
bunits= int(input("Enter current month readings:"))
unit = bunits-aunits
if(unit<=500):
    cost = unit*1.5
elif(unit>500 and unit<=1000):
    cost = unit*3
else:
    cost = unit*5
print("Bill:",cost)

