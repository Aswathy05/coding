#division operation and find the quotient and remainder values. (Without using /, // % operators)
dividend = int(input("Enter Dividend:"))
divisor = int(input("Enter Divisor:"))
q,r =0,0
while(dividend-divisor>=0):
    q += 1
    dividend-=divisor
    r = dividend
print("Quotient:",q)
print("Remainder:",r)
