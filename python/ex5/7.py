#sort string in lexo. order without library functions 
str1 = input("Enter the string:")
res = ""
l1 = len(str1)
for i in range(l1): 
    mini = str1[0] 
    minipos = 0
    for j in range(len(str1)): 
        if(str1[j]<mini):
            mini=str1[j] 
            minipos = j
    str1=str1[:minipos]+str1[minipos+1:] 
    res += mini
print(res)
