t=int(input())
for i in range(t):
    n=int(input())
    s=input()
    c=["b","c","d"]
    v=["a","e"]
    str1=""
    lst1=[]
    lst=[]
    for i in range(len(s)):
        if(i!=(n-1) and (s[i] in c) and (s[i+1] in c)):
            lst.append(s[i])
            lst1.append(lst)
            lst=[]
        else:
            lst.append(s[i])  
    lst1.append(lst)    
    hehe=[]
    for j in lst1:
        if(len(j)==3 or len(j)==2):
            hehe.append(j)  
        else:
            str1=""
            bobo=[]
            for i in range(len(j)):
                if(j[i] in c):
                    bobo.append(j[i])
                    str1+="c"
                elif(j[i] in v):
                    bobo.append(j[i])   
                    str1+="v"
                if(str1=="cv" ):
                    if(i<(len(j)-2) and (j[i+1] in c) and (j[i+2] in v) ):
                        str1=""
                        hehe.append(bobo)
                        bobo=[] 
                    if((i>len(j)-2)):
                        str1=""
                        hehe.append(bobo)
                        bobo=[] 
                elif(str1=="cvc"):
                    str1=""
                    hehe.append(bobo)
                    bobo=[]
    final=[]                
    for i in hehe:
        final.extend(i) 
        final.append(".") 
        
    for i in range(len(final)):
        if(i!=len(final)-1):
            print(final[i],end="")
    print()







""" 













        print(str1,lst,lst1)
        if(s[i] in c):
            str1+="c"
            lst.append(s[i])
        elif(s[i] in v):
            str1+="v"
            lst.append(s[i])
        if(str1=="cvc"):
            str1=""
            lst1.append(lst)
            print(lst1,123456789)
            lst=[]
        elif(str1=="cv" ):
            if(s[i+1]!="c" and s[i+2]!="v" and i!=(len(s)-1)):
                str1=""
                lst1.append(lst)
                lst=[]  
            elif(s[i+1]=="c" and s[i+2]=="v" and i!=(len(s)-1)):
                str1=""
                lst1.append(lst)
                lst=[]    
    print(lst1)        

 """