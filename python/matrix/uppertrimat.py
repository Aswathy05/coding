main_lst=[[1,2,3],[4,5,6],[7,8,9]]
uppertri=[]
for i in range(3):
    lst=[]
    for j in range(3):
        if(j>=i):
            lst.append(main_lst[i][j])
        else:
            lst.append(0)
    uppertri.append(lst)  
print(uppertri)    
for i in uppertri:
    for j in i:
        print(j,end=" ")
    print()          