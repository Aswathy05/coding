def sum_series(n):
    x=0
    global summ
    summ=0
    while(n-x>0):
        summ+=n-x
        x+=2
    return summ
n=int(input("Enter an number:"))   
print(sum_series(n))