import sys
sys.stdin=open("input.txt","r")
sys.stdout=open("output.txt","w")
count=0
inp=[]
for line in sys.stdin:
     if(line[:-1] == '\n'):
           inp.append(line[:-1])
     else:
           inp.append(line) 
lst=[]           
for i in inp:
      lst.append(int(i))          
lst.sort()
for i in lst:
    print(i)