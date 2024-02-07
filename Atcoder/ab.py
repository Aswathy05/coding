n=int(input())
s=input()
count=0
for i in range(0,n-1):
    if(s[i]=="a" and s[i+1]=="b"):
        print("Yes")
        break
    elif(s[i]=="b" and s[i+1]=="a"):
        print("Yes")
        break
else:
    print("No")
        