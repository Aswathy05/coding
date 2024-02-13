import sys
sys.stdin=open("input.txt","r")
sys.stdout=open("output.txt","w")
def hillvalley(l):
    inc=0
    for i in range(1,len(l)-1):
        if(l[i-1]<l[i] and l[i+1]<l[i]):
            inc+=1
        elif(l[i-1]>l[i] and l[i+1]>l[i]):
            inc+=1
    if(inc==1):
        return(True)
    else:
        return(False)
print(hillvalley(list(map(int, input().split()))))

