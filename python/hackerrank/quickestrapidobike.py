lst=input().split()
n=int(lst[0])
p=int(lst[1])
pos=[int(x) for x in input().split()]
time=[int(x) for x in input().split()]
tot=[]
for i in range(n):
    if(p>=pos[i]):
        tot.append((p-pos[i])*time[i])
    else:
        tot.append((pos[i]-p)*time[i])   
print(min(tot))        




