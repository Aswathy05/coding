import sys
sys.stdin=open("input.txt","r")
sys.stdout=open("output.txt","w")

for j in range(int(input())):
    n=int(input())
    abc=[0]*26
    inputLst=input().split()
    for i in range(n):
        inputLst[i]=int(inputLst[i])
    for x in inputLst:
        for ind in range(26):
           if(abc[ind]==x):
                abc[ind]+=1     
                print(chr(97+ind),end="")
                break
    print()   




             

