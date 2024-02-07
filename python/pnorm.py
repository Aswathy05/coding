def norm(v,p=2):
    sum=0
    for i in range(len(v)):
        sum+=(i**p)**(1/p)
        print(sum)
    return sum     
