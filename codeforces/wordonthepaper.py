t=int(input())
for i in range(t):
    lst=[]
    for i in range(8):
        x=input()
        lst.append(x)
    count=0    
    for i in range(8):  #row
        for j in range(8): #column
            if(lst[i][j]!="."):
                column=j
                count+=1
                break
        if(count!=0):
            break    
    word=""            
    for i in range(8):
        if(lst[i][column]!="."):
            word+=(lst[i][column])        
    print(word)           
