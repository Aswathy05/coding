def repfree(s):
    s=list(s) 
    if(len(s)==len(set(s))):
        return(True)
    else:
        return(False)
print(repfree(input()))    

