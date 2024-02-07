import sys
sys.stdin=open("input.txt","r")
sys.stdout=open("output.txt","w")
for i in range(int(input())):
    n=int(input())
    s=input()
    count=0
    i=0
    while(True):
        if(s[i]=="B" and "B" not in s[:i]):
      
            start=i
        if(s[i]=="B" and "B" not in s[i+1:]):
            end=i
            
            break 
        i+=1
    print(end-start+1)       


