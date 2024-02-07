s = input()
upper=0
lower=0
num=0
for i in range(len(s)):
    c=s[i]
    if(c.isupper()):
        upper+=1
    if(c.islower()):
        lower+=1
    if(c.isdecimal()):
        num+=1
print("No of uppercase=",upper)
print("No of lowercase=",lower) 
print("No of numeric values=",num)     
print("No of special characters=",len(s)-(upper+lower+num)) 
                