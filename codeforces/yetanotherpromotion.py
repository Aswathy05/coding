#min number of coins to buy at least n kgs of potatoes
t=int(input())
for i in range(t):
    x=input()
    lst1=x.split()
    a=int(lst1[0])  #price on 1st day   5                                
    b=int(lst1[1])  #price on 2nd day   4
    y=input()
    lst2=y.split()
    n=int(lst2[0])  #req amount of potatoes     3
    m=int(lst2[1])  #amount of potatoes to use the promotion    1
    rem=n-(m+1)                 #rem=3-(1+1)=1
    if(a>=b):
        amt1 = m*a+(rem)*b      #amt1=1*5+1*4=9
        amt2 = n*b              #amt2=3*4
        amt3 = m*a+(rem)*a
        mini=min(amt1,amt2,amt3)
    if(a<b):
        if(n<m):
            amt1 = n*a
        else:
            amt1 = m*a+(rem)*a    
    print(mini)    




