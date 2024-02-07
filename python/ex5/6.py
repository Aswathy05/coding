#count the number of uppercase, lowercase, special characters, numeric values in a string
str1 = input("Enter the string:") 
upp, low, spechr, num = 0, 0, 0, 0 
for i in str1:
    if(i.isupper()): 
        upp+=1
    elif(i.islower()): 
        low+=1
    elif(i.isdecimal()): 
        num+=1
spechr = len(str1) - (upp+low+num) 
print("Uppercase characters:",upp) 
print("Lowercase characters:",low) 
print("Special characters:",spechr) 
print("Numeric values:",num)
