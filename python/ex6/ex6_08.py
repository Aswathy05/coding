#sum of digits using recursive functions
def sumDigits(n):
    if(n==0):
        return 0
    else:
        return (n%10)+sumDigits(n//10)

num = int(input("Enter the number to find sum of digits:"))
ans = sumDigits(num)
print("Sum of digits=",ans)