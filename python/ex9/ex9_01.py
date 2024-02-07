cities={'Chennai':600001,'Delhi':110001,'Bangalore':560001,'Hyderbad':500001,'Ahmedabad':380001,'Lucknow':226001,'Mumbai':400001}
city=input("Enter city name : ")
for i in cities:
    if i == city:
        print("Pincode :",cities[i])