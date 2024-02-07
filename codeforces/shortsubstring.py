t=int(input())
for i in range(t):
    b=input()
    lst1=[]
    for j in range(1,len(b)):
        lst=[]
        if(j%2!=0):
            lst.append(b[j-1])
            lst.append(b[j])
            lst1.append(lst)    
    str1=""
    for j in range(len(lst1)):
        str1+=lst1[j][0]
    print(str1+lst1[len(lst1)-1][1])    

