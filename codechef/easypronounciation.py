t=int(input())
lst=["a","e","i","o","u"]
for i in range(t):
    n=int(input())  #length of string s
    s=input()
    count=0
    for j in s:
        break if(j in lst) else count+=1
    if(count>=4):
        print("no")        
    else:
        print("yes")