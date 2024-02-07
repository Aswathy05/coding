def facts(n=20):
    i=1
    while(i<=n):
        if(n%i==0):
            print(i)
        i+=1
n=int(input("Enter a number:"))
facts(n)            