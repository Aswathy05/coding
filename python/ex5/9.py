#menu driven program with inbuilt functions 
print(""" TYPE,
1	- to find the first occurrence of a substring from the end.
2	- to right justify a string.
3	- to capitalize the first letter of a string.
4	- to check whether the string is alphanumeric.
5	- to partition the given text into three parts""") 
cmd = input("Enter:")
str1 = input("Enter the string:") 
if(cmd=="1"):
    str2 = input("Enter the character to find:") 
    if(str1.rfind(str2)!=-1):
        print(str1.rfind(str2)) 
    else:
        print("Not found.") 
elif(cmd=="2"):
        just = int(input("Enter the number of characters:")) 
        print(str1.rjust(just))
elif(cmd=="3"): 
        print(str1.capitalize())
elif(cmd=="4"):
    if(str1.isalnum()):
            print("It is an alphanumeric string.") 
    else:
            print("It isnt an alphanumeric string.")
else:
    str2 = input("Enter the partition text:") 
    print(str1.partition(str2))
