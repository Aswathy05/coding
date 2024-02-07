employees = {1: ['Niranjan', '01/01/2004', 1000.0],
             2: ['Nithish', '02/02/2003', 1500.0],
             3: ['Bharathi', '03/03/2003', 2000.0],
             4: ['Yhokesh', '04/04/2006', 2500.0],
             5: ['Titus', '05/05/2002', 3000.0],
             6: ['Anierudh', '06/06/1999', 3500.0]}
print('Original dictionary :',employees)
employees[2] = ['Anish', '07/07/1996', 4000.00]
print('1. Insert a new employee details as the second employee :')
print(employees)
del employees[4]
print('2. Delete the employee at the 4th position :')
print(employees)
last_emp = max(employees.keys())
del employees[last_emp]
print('3. Delete the last employee :')
print(employees)
for i in employees:
    employees[i][2] = employees[i][2] * 1.05
print('4. Increment the salary of all employees by 5% :')
print(employees)