t=int(input())
s=input().split()
num=[]
lst=[s[0]]
for i in range(t-1):
    if(int(s[i])<int(s[i+1])):
        lst.append(s[i+1])   
    elif(int(s[i])==int(s[i+1])):
        lst.append(i+1)
        num.append(len(lst))     
        lst[:]=[]
    else:
        print(lst,num)
        num.append(len(lst))
        lst[:]=[]
s1=s[sum(num):]     
print(s1)
num.append(len(s1))
print(num)
print(max(num))        