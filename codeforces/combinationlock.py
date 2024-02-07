n=int(input())
a=input()
b=input()
count=0
for i in range(n):
    if((int(a[i])-int(b[i]))<0):
        if(((9-int(b[i])+int(a[i])-0)+1)<(int(b[i])-int(a[i]))):
            count+=9-int(b[i])+int(a[i])-0+1
        else:    
            count+=int(b[i])-int(a[i])
    else: 
        if(((9-int(a[i])+int(b[i])+1)-0)<(int(a[i])-int(b[i]))):
            count+=9-int(a[i])+int(b[i])-0+1
        else:       
            count+=int(a[i])-int(b[i])  
print(count)    
