s=input()
count=0
ch=set(s)
for i in ch:
    if(i=="{"):
        continue
    elif(i=="}"):
        continue 
    elif(i==" "):
        continue 
    elif(i==","):
        continue  
    else:     
        count+=1
print(count)        