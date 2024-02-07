t=int(input())
for i in range(t):
    n=int(input())
    s=input()
    lst=s.split()
    lenlst=len(lst)//2
    if(n%2==0):
        count1,count2=0,0
        for j in lst[0:lenlst]:
            if(j=="1"):
                count1+=1
            if(j=="2"):
                count2+=1
        count3,count4=0,0 
        for j in lst[lenlst:len(lst)]:
            if(j=="1"):
                count3+=1
            if(j=="2"):
                count4+=1  
        if(count1*count2 == count3*count4):
            if(count2!=0):
                print("2")
            else:
                print("1")   
        else:
            print("-1") 
    else:
        print("-1")       




