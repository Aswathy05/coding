t=int(input())
for i in range(t):
    n=int(input())
    lst=input().split()
    lst1=[]
    for i in lst:
        lst1.append(int(i))
    count=0    
    if(n%2==0):
        while(len(lst1)>0):
            maxi=max(lst1)
            mini=min(lst1)
            diff=maxi-mini
            count+=diff
            lst1.remove(maxi)
            lst1.remove(mini)
    else:
        while(len(lst1)>1):
            maxi=max(lst1)
            mini=min(lst1)
            diff=maxi-mini
            count+=diff
            lst1.remove(maxi)
            lst1.remove(mini)
    print(count)        


