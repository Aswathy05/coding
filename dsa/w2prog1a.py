def threesquares(x):
    while(True):
        if(x%4!=0):
            break
        else:
            x=x//4      
    if(x%8==7):
        return(False)
    else:
        return(True)
for i in range(int(input())):
    print(threesquares(int(input())))    
    
