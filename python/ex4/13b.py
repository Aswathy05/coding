# print the sequence ----  -4,-2,0,2,4..

i = -4
n = int(input("Enter number of terms:"))
for j in range(n):
    if (j!=n-1):
        print(i,end=",") 
    else:
        print(i)
    i+=2