#gcd using recursive function
def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)
    
a,b = int(input("Enter n1:")), int(input("Enter n2:"))
print("Gcd:",gcd(a,b))