t=int(input())
for i in range(t):
    s=input()
    str1=""
    i=0
    while(i<=(len(s)//3)+1):
        str1+="Yes"
        i+=1   
    if s in str1:
        print("yes")
    else:
        print("no")        