def addpoly(p1,p2):
    dict1={}
    for i in p1:
        if i[1] not in dict1:
            dict1[i[1]]=i[0]
        else:    
            dict1[i[1]]+=i[0]
    for i in p2:
        if i[1] not in dict1:
            dict1[i[1]]=i[0]
        else:    
            dict1[i[1]]+=i[0]
    add_Lst=[]    
    for i in sorted(dict1.items()):
        if(i[1]!=0):
            add_Lst.append((i[1],i[0]))    
    return(add_Lst[::-1])        

print(addpoly([(4,3),(3,0)],[(-4,3),(2,1)]))

def multpoly(p1,p2):
    mul_Lst=[]
    for i in p1:
        for j in p2:
            coeff=i[0]*j[0]
            power=i[1]+j[1]
            mul_Lst.append((coeff,power))
    mul_dict={}        
    for i in mul_Lst:
        if i[1] not in mul_dict:
            mul_dict[i[1]]=i[0]
        else:  
            mul_dict[i[1]]+=i[0]  
    finalMulLst=[]        
    for i in mul_dict:
        if(mul_dict[i]!=0):
            finalMulLst.append((mul_dict[i],i))       
    return(finalMulLst)    
