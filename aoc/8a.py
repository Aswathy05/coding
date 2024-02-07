t=int(input())
rl=input()
rl=rl*100
empty=input()
nodes=[]
for i in range(t):
    s=input().split()
    lst=[]
    for i in range(len(s)):
        lst.append(list(s[i]))
    lst[2].remove("(")
    lst[2].remove(",")
    lst[3].remove(")")  
    nodes.extend([[lst[0],lst[2],lst[3]]])
  

def rlCheck(node,i,j):
    while(True):
        if(node=="Z","Z","Z"):
             break
        if(nodes[i][0]==node):
                print(node)
                if(rl[j]=="R"):
                    check=nodes[i][1]
                    j+=1
                else:
                    check=nodes[i][2] 
                    j+=1
                i+=1    
                return(check)    
node=["A", "A", "A" ] 
i,j=0,0 
check=rlCheck(node,i,j)
""" i=rlCheck(i)
j=rlCheck(j) """
node=check
print(node,i,j)





 
    
