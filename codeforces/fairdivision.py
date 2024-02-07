t=int(input())
for j in range(t):
    n=int(input())
    a=input().split()
    lst=[]
    for i in a:
        lst.append(int(i))
    summ=sum(lst)
    count=0
    for i in lst:
        if(i==1):
            count+=1
            break
    if(summ%2==0):
        if(count==1):
            print("yes")
        elif(n%2==0):
                print("yes")
        else:
            print("no")        
    else:
        print("no")
    '''one,two=0,0
    for j in a:
        if(j=="1"):
            one+=1
        else:
            two+=1
    if(one%2!=0):
        print("no") 
    if(two%2!=0 and one%2==0):
        print("no")     
    else:
        print("yes")      '''