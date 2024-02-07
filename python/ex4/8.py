#Voltage program
volt=5
while(volt==5):
    volt=int(input("Enter voltage:"))
    if(volt>5):
        print("Breakdown voltage")
    elif(volt<5):
        print("Cutoff voltage")    
    else:
        print("Active")    