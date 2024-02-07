#232323 sum1=2+2+2=6 sum2=3+3+3=9
s=input()
slen=len(s)
count=0
count1=0
for i in range(slen):
    if(i%2==0):
        count+=int(s[i])
    else:
        count1+=int(s[i])
print(count,count1)            
