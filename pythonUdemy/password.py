import random
import string
lower=list(string.ascii_lowercase)
upper=list(string.ascii_uppercase)
numbers=[0,1,2,3,4,5,6,7,8,9]
for i in numbers:
    numbers[i]=str(numbers[i])
splChar=list(string.punctuation)


l=int(input("How many lowercase letters do you want? "))
u=int(input("How many uppercase letters do you want? "))
n=int(input("How many numbers do you want? "))
s=int(input("How many special characters do you want? "))

password=""
for i in range(l):
    password+= random.choice(lower)
for i in range(u):
    password+= random.choice(upper)
for i in range(n):
    password+= random.choice(numbers)
for i in range(s):
    password+= random.choice(splChar)
password=list(password)   
random.shuffle(password)    
print(*password,sep="")

