lst=[1,11,111,1111,2,22,222,2222,3,33,333,3333,4,44,444,4444,5,55,555,5555,6,66,666,6666,7,77,777,7777,8,88,888,8888,9,99,999,9999]
t=int(input())
for j in range(t):
    x=int(input())
    lst1=[]
    for i in lst:
        lst1.append(i)
        if(x==i):
            break
    count=0          
    for i in lst1:
        for j in str(i):
            count+=1 
    print(count)            