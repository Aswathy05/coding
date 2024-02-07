t=int(input())
for i in range(t):
    n=int(input())
    x=input().split()
    i=0
    O=0
    while(True):
        if(i>=n):
            break
        if(x[i]=="O"):
            O+=1
            print(n)
            break
        i+=1
    if(O==0):
        A,B,AB=0,0,0
        for i in x:
            if(i=="A"):
                A+=1
            elif(i=="AB"):
                A+=1
                B+=1
                AB+=1
            elif(i=="B"):
                B+=1
        print(max(A,B,AB))

      