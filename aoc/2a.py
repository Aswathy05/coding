n=int(input())
sum=0
for i in range(n):
    s=input().split()
    id=s[1]
    id=int(id[:len(id)-1])
    s.remove(s[0])
    s.remove(s[0])
    red,blue,green=0,0,0
    for i in range(len(s)):
        if(s[i]=="blue" or s[i]=="blue," or s[i]=="blue;"):
            if(int(s[i-1])>blue):
                blue=int(s[i-1])
        elif(s[i]=="red" or s[i]=="red," or s[i]=="red;"):
            if(int(s[i-1])>red):
                red=int(s[i-1])
        elif(s[i]=="green" or s[i]=="green," or s[i]=="green;"):
            if(int(s[i-1])>green):
                green=int(s[i-1])           
    if(red<=12 and green<=13 and blue<=14 ):
        sum+=int(id)
print(sum)    

              

