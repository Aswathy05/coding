sum=0
for i in range(1000):
    s=input()
    for i in s:
        if(i.isdigit()):
            first=i
            break
    for i in s[::-1]:
        if(i.isdigit()):
            last=i
            break 
    digit=first+last 
    sum+=int(digit)
print(sum)
