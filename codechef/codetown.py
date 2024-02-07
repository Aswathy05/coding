vowel=["A","E","I","O","U"]
t=int(input())
for i in range(t):
    s=input()
    count=0
    for i in range(len(s)):
        if(i%2==0 and s[i] not in vowel):
            count+=1
        elif(i%2!=0 and i!=7 and s[i] in vowel):
            count+=1
        elif(i==7 and s[i] not in vowel):
            count+=1  
    if(count==8):
        print("yes")
    else:
        print("no")                   
