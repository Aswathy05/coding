import sys
sys.stdin=open("input.txt","r")
sys.stdout=open("output.txt","w")


for j in range(int(input())):
    n,k=(int(i) for i in input().split())
    lst=[]
    for i in range(1,n+1):
        lst.append(i)
    odd=[1,3,5,7]
    i=1
    new=[]
    while(True):
        for k in odd:
            for z in range(1,len(lst)+1):
                if(z==i*k and (lst[z-1] not in new)):
                    new.append(lst[z-1])
            if(len(new)==len(lst)):
                break         
        if(len(new)==len(lst)):
            break         
        i+=1
    print(new)
            
        

        