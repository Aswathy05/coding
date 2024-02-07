T=(1,3,2,4,6,5)
t=()
for i in range(len(T)):
    if i%2!=0:
        t+=(T[i],)
print(t)