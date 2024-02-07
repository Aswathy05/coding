str1 = input("Enter the string:") 
str2 = ""
l1 = len(str1)
for i in range(l1-1,-1,-1): 
    str2+=str1[i]
if(str1==str2):
    print("The given string is a palindrome") 
else:
    print("The given string is not a palindrome")
