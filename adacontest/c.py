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
lib=[]  
ver=[]
for k in range(len(inp)):
    var=inp[k].split(",")
    hehe=var[1]
    haha=var[2]
    lib.append(hehe[0:len(hehe)])
    if(k==len(inp)-1):
          ver.append(haha[0:len(haha)])  
    else:       
        ver.append(haha[0:len(haha)-1]) 
dict1 = {}
chumma = []
for k,v in zip(lib, ver):
    if(k in chumma):
         if(v<dict1[k]):
             dict1[k] = v
    else:
        dict1[k] = v
        chumma.append(k)          
for i in dict1:
    print(i,":",dict1[i],sep="") 
