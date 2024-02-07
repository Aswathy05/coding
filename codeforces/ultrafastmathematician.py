x=input()
y=input()
str=""
for i in range(len(x)):
        if x[i]!=y[i]:
            str+="1"        
        else:
            str+="0"
print(str)               