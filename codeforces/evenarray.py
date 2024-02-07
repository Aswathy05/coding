t=int(input())
for i in range(t):
    n=int(input())
    a=input().split()
    lst=[]
    for j in a:
        lst.append(int(j))
    dict={}
    for j in range(len(lst)):
        if(j%2!=lst[j]%2):
            dict[j%2]=lst[j]%2
    print(dict)
             
