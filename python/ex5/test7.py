#hello 
s=input()
ch=input()
str2=""
for i in range(len(s)):
    str1=s[i]
    if(str1!=ch):
        str2+=str1
print(str2)       
