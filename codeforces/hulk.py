n=int(input())
str1="I hate "
for i in range(1,n+1):
    if(i%2==0):
        str1+="that I love "
    elif(i%2!=0 and i>1):
        str1+="that I hate "       
str1+="it" 
print(str1)       



