def print_reverse(Lst):
    Lst2=[]
    for i in range(len(Lst)-1,-1,-1):
        Lst2.append(Lst[i])
    print("The Reversed list is",Lst2)
Lst=eval(input("Enter the list:"))
print_reverse(Lst)





