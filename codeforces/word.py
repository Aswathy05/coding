s=input()
up,low=0,0
for i in s:
    if i.isupper():
        up+=1
    elif i.islower():
        low+=1
if(up>low):
    print(s.upper())  
else:
    print(s.lower())                   
