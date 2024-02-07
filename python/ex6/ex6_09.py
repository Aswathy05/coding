# n + (n-2) + (n-4) .. (n-x)<=0 using recursive funtion
def sum_series(n):
    if(n < 0):
        return 0
    else:
        return n+sum_series(n-2)

num = int(input("Enter n for sum of series:"))
ans = sum_series(num)
print("Result:",ans)