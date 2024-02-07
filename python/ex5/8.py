#program to remove all occurences of a character in a string 
str1 = input("Enter the string:")
char = input("Enter the character to be removed:") 
str2 = ""
for i in str1: 
    if(i!=char):
        str2+=i
print("String after removing", char, "is", str2)
