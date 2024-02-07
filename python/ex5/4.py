str1 = input("Enter the string:") 
substr = input("Enter the substring:") 
count = 0
l1 = len(str1) 
l2 = len(substr)
for i in range(l1 - l2 + 1): 
    if(str1[i:i+l2]==substr):
        print(i,end=" ") 
        count+=1
if(count!=0):
    print()
    print(substr,"is repeated",count,"times in",str1) 
else:
    print("Not found")

