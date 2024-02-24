def remdup(l):
    uniqLst=[]
    for i in l:
        if(i not in uniqLst):
            uniqLst.append(i)
    return(uniqLst)
print(remdup([3,5,7,5,3,7,10]))
        