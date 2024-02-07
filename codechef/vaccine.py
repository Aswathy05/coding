T=int(input())
for i in range(T):
    a=input()
    lst=a.split()
    D=int(lst[0])
    L=int(lst[1])
    R=int(lst[2])
    if(D<L):
        print("Too Early")
    elif(D>R):
        print("Too Late") 
    else:
        print("Take second dose now")       
