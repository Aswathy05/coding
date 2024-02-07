n=int(input())
lst=[]
spl=["!","@","#","$","%","^","&","*","+","-"]
for i in range(n):
    s=input()
    lst.append(s)
    
































sumLst=[]    
for i in range(len(lst)):
    for j in range(len(lst[i])):
        if(lst[i][j] in spl):
            if((lst[i-1][j-1]).isdigit()):
                if(int(lst[i-1][j-1]) not in sumLst):
                    sumLst.append(int(lst[i-1][j-1]))
            elif((lst[i-1][j]).isdigit()):
                if(int(lst[i-1][j]) not in sumLst):
                        sumLst.append(int(lst[i-1][j]))
            elif((lst[i-1][j+1]).isdigit()):
                if(int(lst[i-1][j+1]) not in sumLst):
                        sumLst.append(int(lst[i-1][j+1]))
            elif((lst[i+1][j-1]).isdigit()  ):
                if(int(lst[i+1][j-1]) not in sumLst):
                        sumLst.append(int(lst[i+1][j-1]))
            elif((lst[i+1][j]).isdigit()):
                if(int(lst[i+1][j]) not in sumLst):
                        sumLst.append(int(lst[i+1][j]))
            elif((lst[i+1][j+1]).isdigit()):
                if(int(lst[i+1][j+1]) not in sumLst):
                        sumLst.append(int(lst[i+1][j+1]))
            elif((lst[i][j-1]).isdigit()):
                if(int(lst[i][j-1]) not in sumLst):
                        sumLst.append(int(lst[i][j-1]))
            elif((lst[i][j+1]).isdigit()):
                if(int(lst[i][j+1]) not in sumLst):
                        sumLst.append(int(lst[i][j+1]))
print(sumLst)            
 

            



