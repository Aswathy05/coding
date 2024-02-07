d1={'a':100,'b':200,'c':300}
d2={'a':300,'b':200,'d':400}
d={}
for i in d1:
    for j in d2:
        if i==j:
            d1[i]+=d2[i]
        else:
            d[j]=d2[j]
d.update(d1)
print('New dictionary :',d)
print('Keys :',d.keys())
print('Values :',d.values())
print('Key-Value pairs : ',d.items())