t=int(input())
for j in range(t):
    b=input()
    lst=[]
    for i in range(8):
        s=input()
        lst.append(s)
    for i in range(1,7):
        for j in range(1,7):
            if(lst[i][j]=="#"):
                if(lst[i+1][j+1]=="#" and lst[i+1][j-1]=="#" and lst[i-1][j+1]=="#" and lst[i-1][j-1]=="#"):
                    print(i+1,j+1)      
                    break

