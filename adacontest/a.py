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
for i in inp:
    var=i.split(",")
    three=0
    k=0
    for j in var:
        if(k==0):          
            str1=j.split()         
            if(str1[len(str1)-1]=="Server"):
                three+=1
        if(k==1):
            str1=j.split()
            if(str1[len(str1)-1]=="Library"):
                three+=1
        if(k==2):
            if(j[1]=="v" and j[2: len(j)-1].isdigit()==True):
                three+=1
        if(k==2):
            k=0
        else:            
            k+=1              
        if(three==3):
            count+=1
print(count)
                    
