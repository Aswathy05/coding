s=input()           #1+1+3+1+3
lst=s.split("+")
lst.sort()          #1,1,1,3,3
for i in range(len(lst)):
        print(lst[i],end="+") if(i<len(lst)-1) else print(lst[i])