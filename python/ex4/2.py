#sum of all digits of a number
n = int(input("Enter a number:"))
sum = 0
while(n>0):
    sum+=(n%10)
    n//=10
    if(sum>=10 and n%10==n):
        n = sum + n
        sum=0
print("Sum of digits is",sum)