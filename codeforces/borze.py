n=input()
lst=[]
str1=""
if(n[0]=="."):
    str1+="0"
for i in range(0,len(n)):
    if(n[i]=="-" and n[i+1]=="-"):
        str1+="2"
        lst.append("--")
    elif(n[i]=="-" and n[i+1]=="."):    
        str1+="1"
        lst.append("-.")
    elif(n[i]=="." and n[i+1]=="."):
        str1+="0"
        lst.append(".")
print(lst)        
