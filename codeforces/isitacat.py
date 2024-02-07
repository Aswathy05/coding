t=int(input())
for i in range(t):
    n=int(input())
    s=input()
    lst=[]
    for i in s:
        lst.append(i)
    meow=[]      
    for i in lst:
        if(i=="m" or i=="M"):
            if("m" not in meow):
                meow.append("m")
        elif(i=="e" or i=="E"):
            if("e" not in meow):
                meow.append("e")
        elif(i=="o" or i=="O"):
            if("o" not in meow):
                meow.append("o")
        elif(i=="w" or i=="W"):
            if("w" not in meow):
                meow.append("w")   
        else:
            meow.append(i)                               
    if(len(meow)==4):             
        if((meow[0]=="m") and ( meow[1]=="e") and (meow[2]=="o") and (meow[3]=="w")):
            print("yes")
        else:
            print("no")
    else:
        print("no")     
            

