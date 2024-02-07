t=int(input())
for j in range(t):
    key=input()
    str1=input()
    lst=[]
    for i in range(str1):
        if(i in key):
            lst.append(int(i))
    print(lst)        