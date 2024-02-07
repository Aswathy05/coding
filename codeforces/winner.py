import sys
sys.stdin=open("input.txt","r")
sys.stdout=open("output.txt","w")
dict={}
mikeLst,andrewLst=[],[]
for i in range(1,int(input())+1):
    name,score=input().split()
    if(name=="mike"):
        dict["m"+str(i)]=(int(score))
        mikeLst.append(int(score))
    else:
        dict["a"+str(i)]=(int(score))
        andrewLst.append(int(score))
if(sum(mikeLst)==sum(andrewLst)):
    maxi=sum(mikeLst)        
    mike,andrew=0,0
    for i in dict:
        if(i[0]=="m"):
            mike+=int(dict[i])
        else:
            andrew+=int(dict[i])    
        if(mike==maxi):
            print("mike")
            break
        elif(andrew==maxi):
            print("andrew")
            break    

