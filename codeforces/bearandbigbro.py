x=input()
lst=x.split()
w1=int(lst[0])       
w2=int(lst[1])
count=0
while(w1 <= w2):
    count+=1 
    w1*=3
    w2*=2
print(count)
