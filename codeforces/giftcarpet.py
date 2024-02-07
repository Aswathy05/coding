t=int(input())
for k in range(t):
    x=input().split()
    n=int(x[0])
    m=int(x[1])
    lst1=[]
    for j in range(n):
        s=input()
        lst=[]
        for i in range(m):
            lst.append(s[i])
        lst1.append(lst) 
    result=[]    
    for i in range(m):
        lst2=[]
        for j in range(n):
            lst2.append(0)
        result.append(lst2)     
    for i in range(m):
        for j in range(n):
            result[i][j]=lst1[j][i]    

    dict={}     
    for i in range(m):
        for j in range(n):
            if(result[i][j]=="v"):
                if("v" not in dict):
                    dict["v"]=i               
            elif(result[i][j]=="i"):
                if("i" not in dict and "v" in dict):
                    dict["i"]=i
            elif(result[i][j]=="k"):
                if("k" not in dict and "i" in dict):
                    dict["k"]=i
            elif(result[i][j]=="a"):
                if("s" not in dict and "k" in dict):
                    dict["a"]=i
    index=[]                
    for i in dict:
        index.append(dict[i])
    print(index)    



