a=input()
count=0
for i in range(1,len(a)):
    a,b=((ord(a[i]))-(ord(a[i-1]))),ord("z")-((ord(a[i]))-(ord(a[i-1])))
    if(a>=0 and b>=0):
        count+=min(a,b)
    else:
        if(a>=0):
            count+=a    
        else:
            count+=b    
print(count)
    