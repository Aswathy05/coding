t=int(input())
for i in range(t):
    a,b=input().split()
    #S=0 M=1 L=
    if(a!="M"):
        if(a[len(a)-1]=="S"):
            a="S"
        else:
            a="L"    
    if(b!="M"):
        if(b[len(b)-1]=="S"):
            b="S"
        else:
            b="L"    

    if(a==b):
        print("=")     
    elif(a=="L" and b=="S"):
        print(">")
    elif(a=="S" and b=="L"):
        print("<")
    elif(a=="M")               
    