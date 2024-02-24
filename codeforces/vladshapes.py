import sys
sys.stdin=open("input.txt","r")
sys.stdout=open("output.txt","w")

for j in range(int(input())):
    n=int(input())
    row=[]
    for i in range(n):
        s=input()
        one=0
        for i in s:
            if(int(i)==1):
                one+=1
        if(one!=0):
            row.append(one)

    if(len(set(row))==1):
        print("SQUARE")
    else:
        print("TRIANGLE")