#Engagementarrangementmanagementcommitment
s = input()
f = input()
slen=len(s)
flen=len(f)
count=0
for i in range(slen):
    r=s[i:i+flen]
    if(r==f):
        print(i)
        count+=1    
print(count)
