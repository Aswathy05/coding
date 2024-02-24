import sys
sys.stdin=open("input.txt","r")
sys.stdout=open("output.txt","w")


for j in range(int(input())):
    n=int(input())
    a=input().split()
    lst=[]
    for i in a:
        binary=bin(int(i))[2:]
        lst.append(binary)
    print(lst)
    outer=[]
    for i in range(n-1):
        count=0
        inner=[]
        for j in range(i+1,n):
            """ print(lst[i],lst[j]) """
            if(len(lst[i])>len(lst[j])):
                lst[i],lst[j]=lst[j],lst[i]
            no=0
            for z in range(len(lst[i])):
                """ print(lst[i][z],lst[j][z]) """
                if(lst[i][z]==lst[j][z]):
                    no=1
                    break
            if(no!=0):
                
                inner.append(lst[j])
            
        outer.append(inner)
    print(outer)



        


