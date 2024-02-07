s=input()
slen=len(s) #good
a=0
for i in range(slen):
    temp1=s[i]
    for j in range(i+1,slen):
        temp2=s[j]     
        if(temp1==temp2):
            a=1
            break
if(a==1):
    print("BAD") 
if(a==0):
    print("GOOD")               


