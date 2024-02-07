s=input()
t=input()
rev=""
for i in s[::-1]:
    rev+=i
if(rev==t):
    print("YES")
else:
    print("NO")    