def freq(s):
    l=list(s)
    d={}
    for i in s:
        c=0
        for j in s:
            if i==j: 
                c+=1
        if i not in d:
            d[i]=c
    return d
s=input("Enter a string : ")
print("Frequency of each character : ")
print(freq(s))