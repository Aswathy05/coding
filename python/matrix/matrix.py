#mat=[[1,2,3],[4,5,6],[7,8,9]]
main_lst=[]
for i in range(3):
    lst=[]
    for j in range(3):
        x=int(input())
        lst.append(x)
    main_lst.append(lst)
for i in main_lst:
    for j in i:
        print(j,end=" ")
    print()