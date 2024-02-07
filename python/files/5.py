import keyword
with open("code.txt","r") as f:
    words=f.read().split()
    for i in words:
        if(i in keyword.kwlist):
            print(i)