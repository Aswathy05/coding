y=input()
y1=int(y)+1
while(len(set(str(y1)))!=4):
    y1+=1
print(y1)