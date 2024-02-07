#program to calculate the bonus and display the total salary
sal = int(input("Enter the salary:"))
gen = int(input("Enter gender (1 for male, 2 for female):"))
netsal = sal
if(gen==1):
    netsal += sal*(5/100)
else:
    netsal += sal*(15/100)
if(sal < 10000):
    netsal += sal*(2/100)
print("The net salary is:",netsal)

