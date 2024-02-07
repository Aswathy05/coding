main_lst=[]
for i in range(3):
    lst=[]
    for j in range(3):
        if(i==j):
            lst.append(1)
        else:
            lst.append(0)
    main_lst.append(lst)  
for i in main_lst:
    for j in i:
        print(j,end=" ")
    print()          