import sys
sys.stdin=open("input.txt","r")
sys.stdout=open("output.txt","w")
inp=[]
for line in sys.stdin:
    if(line[:-1] == '\n'):
        inp.append(line[:-1])
    else:
        inp.append(line) 
count=0      
lst=[]  
str1=""
for k in inp:
    var=k.split(",")
    hehe=var[0].split()
    lst.append(hehe[0:len(hehe)-1])
lst1=[]    
for i in lst:
    if(i not in lst1):
        lst1.append(i)
print((lst1))        