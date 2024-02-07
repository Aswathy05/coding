str1=input()
str2=input().split()
lst=[]
for i in str2:
    for j in i:
        lst.append(j)
for i in lst:
    if(i in str1):
        print("yes")
        break        
else:
    print("no")        