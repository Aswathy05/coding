with open("t1.txt","w+") as f:
    f.write("This is Aswathy")
    f.seek(0)
    print(f.read())
with open("t1.txt","a+") as f:
    f.write("\nI am 18 years old")
    f.seek(0)
    data=f.read()
    up,low,num=0,0,0
    for i in data:
        if(i.isupper()):
            up+=1
        elif(i.islower()):
            low+=1
        elif(i.isdigit()):
            num+=1
    print(up,low,num)        
