# cook your dish here
import math
for i in range(int(input())):
    x,y=(int(i) for i in input().split())
    print(math.gcd(x,y))