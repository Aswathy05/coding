#prime number
for i in range(1,10):
    if(i==1):
        pass
    for j in range(2,i):
        if(i%j==0):
            break
    else:
        print(i)    