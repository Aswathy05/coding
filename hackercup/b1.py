import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

t=int(input())
for z in range(t):
    n = int(input())
    y=input().split()
    lst=[]
    for i in y:
        lst.append(int(i))
    x=sorted(lst)
    if(n==5):
        min1=(x[2]+x[0])/2
        max1=((x[n-1]+x[n-2])/2)
        min2=(x[1]+x[0])/2
        max2=((x[n-1]+x[n-3])/2)
        if(max1-min1 >=max2-min2):
            santasWalk=max1-min1
        else:
            santasWalk=max2-min2
    else:
        min=(x[1]+x[0])/2
        max=((x[n-1]+x[n-2])/2)
        santasWalk=max-min
    print("Case #" + str(z+1) + ": " + str(santasWalk))    

  