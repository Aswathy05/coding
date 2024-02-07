#Gunanicaa's Election
t=int(input())
for i in range(t):
    dic = {}
    s = input()
    res=0
    for i in s:
        if i not in dic:
            dic[i]=1
        else:
            dic[i]+=1
    for i in dic:
        freqsum=0
        for j in dic:
            if i!=j:
                freqsum+=dic[j]
        if(freqsum==dic[i]):
            res=1
            break

    if(res==1):
        print("YES")
    else:
        print("NO")

