lst = []
num = int(input())
i=1
while(i*i<=num):
    """ print(i) """
    if(num%i==0):
        lst.append(i)
        lst.append(int(num/i))
    i+=1
print(lst)