import sys
sys.stdin=open("input.txt","r")
sys.stdout=open("output.txt","w")
t=int(input())
for i in range(t):
    n,k=(int(i) for i in input().split())
    a=input().split()
    lst=[]
    for i in a:
        if(int(i)>=k):
            lst.append(int(i)%k)
    if(len(lst)!=0):
        print(min(lst)) 
    else:
        print(-1)           
