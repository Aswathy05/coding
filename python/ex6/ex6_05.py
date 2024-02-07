#Sine series using function
def sum_series(x,num):
    count=1
    sign=1
    sum=0
    for i in range(num):
        product = 1
        for j in range(1, count+1):
            product*=j
        sum+=(x**count)*sign/product
    sign=sign*-1
    count+=2
    return sum
x=int(input("Enter number :"))
num=int(input("Enter limit:"))
sum1= sum_series(x, num)
print(sum1)