t=int(input())
for i in range(t):
    s=input()
    zero=["y","Y"]
    one=["e","E"]
    two=["s","S"]
    if((s[0] in zero) and (s[1] in one) and (s[2] in two)):
        print("yes")    
    else:
        print("no")    