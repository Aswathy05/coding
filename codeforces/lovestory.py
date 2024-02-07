t=int(input())
for i in range(t):
    str1="codeforces"
    str2=input()
    count=0
    for i in range(len(str1)):
        if(str1[i]!=str2[i]):
            count+=1
    print(count)        
