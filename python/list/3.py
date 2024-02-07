n=int(input("Enter the number of elements in the list:"))
arr=[]                          #arr=1 2 3
for i in range(n):
    x=int(input("Enter the element:"))
    arr.append(x)
prod_list=[]     
for i in range(len(arr)):   
    prod=1  
    for j in range(len(arr)):
        if(i==j):
            continue
        else:
            prod*=arr[j]
    prod_list.append(prod)       
print(prod_list)        
    
