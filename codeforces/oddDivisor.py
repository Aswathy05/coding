import sys
sys.stdin=open("input.txt","r")
sys.stdout=open("output.txt","w")

for i in range(int(input())):
    n=int(input())
    while(n%2==0):
        n=n//2  
                  
    if(n==1):
        print("NO")
    else:
        print("YES")        