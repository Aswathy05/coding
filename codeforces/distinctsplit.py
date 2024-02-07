t=int(input())
for i in range(t):
    n=int(input()) #length of the string
    s=input() #string
    for j in range(n):
        temps=s[j]
        for k in range(j+1,n):
            temps2=s[k]
            if(temps==temps2):
                ind=k
    x=s[0:k]
    y=s[k:n]
    countx=0
    county=0
    for j in range(len(x)):
        if(x[j] not in x[0:j]+x[j+1:]):
            countx+=1

    print(x)