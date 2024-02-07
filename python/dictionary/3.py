d1={'a':100,'b':200,'c':300}
d2={'a':300,'b':200,'d':400}
dict={}
for i in d1:
    for j in d2:
        if(i==j):
            d1[i]+=d2[i]
        else:
            dict[j]=d2[j]  
dict.update(d1)          
print(dict)        
print("keys:",dict.keys())
print("values:",dict.values())
print("items:",dict.items())
