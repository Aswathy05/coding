n=int(input())
s=input().split()
hard=0
for i in range(n):
    if(s[i]=="1"):
        hard+=1
if(hard!=0):
    print("hard")
else:
    print("easy")    