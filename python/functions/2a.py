#to find if a given number is prime or not
n=int(input())
for i in range(2,n):
    if(n%i==0):
        print("np")
        break
else:        
    print("p")        
