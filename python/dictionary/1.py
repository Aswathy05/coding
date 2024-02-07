n=int(input("Enter the number of cities:"))
dict={}
for i in range(n):
    city=input("city name:")
    pin=input("Enter pincode:")
    dict[city]=pin
city=input("Enter the cityname for which you need the pincode:")    
for i in dict:
    if(i==city):
        print("The pincode is:",dict[i])


        
