x=input()
lst=x.split()
a=int(lst[0])
b=int(lst[1])
c=int(lst[2])
d=int(lst[3])
e=int(lst[4])
count=0
if(a<40):      
    count+=1
if(b<40):
    count+=1    
if(c<40):
    count+=1    
if(d<40):
    count+=1
if(e<40):
    count+=1  
if(count>=3):
    print("YEARLAG")
else:
    print("CAZZ")       






'''if(a<40 and b<40 and c<40 or d<40 or e<40):
    print("YEARLAG")
elif(b<40 and c<40 and d<40 or a<40 or e<40):
    print("YEARLAG")
elif(c<40 and d<40 and e<40 or a<40 or b<40):
    print("YEARLAG")
elif(d<40 and e<40 and a<40 or b<40 or e<40):
    print("YEARLAG")
elif(e<40 and a<40 and b<40 or c<40 or d<40):
    print("YEARLAG")    
else:
    print("CAZZ")   '''  