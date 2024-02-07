#finding the exponent value from base and power 
base = int(input("What base? ")) 
str1 = "What power of " + str(base) + "?" 
power = int(input(str1)) 
res = base**power 
print(base, "to the power of", power,"is",res) 