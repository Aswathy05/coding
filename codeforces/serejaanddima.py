n=int(input())
lst=input().split()
s,d=0,0
turn=0
while(len(lst)!=0):
    if(int(lst[0])>int(lst[len(lst)-1])):
        if(turn%2==0):
            s+=int(lst[0])
        else:
            d+=int(lst[0])
        del lst[0]
    else:
        if(turn%2==0):
            s+=int(lst[len(lst)-1])
        else:
            d+=int(lst[len(lst)-1])  
        del lst[len(lst)-1] 
    turn+=1     
print(s,d)    



