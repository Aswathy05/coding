str1=input()
slen = len(str1)
temp = ""
ind = 0
for i in range(slen):
    val = str1[0]
    for j in range(len(str1)):
        if(str1[j]<=val):
            val=str1[j]
            ind = j
    temp += val
    str1 = str1[0:ind]+str1[ind+1:len(str1)]
    print(str1)
print(temp,123)