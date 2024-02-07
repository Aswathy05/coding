lst=[]
for i in range(5):
    a=input().split()
    lst.append(a)   
for i in range(5):          #i=row
    for j in range(5):      #j=column
            count=0
            if(lst[i][j]=="1"):
                if(i<=2):
                    count+=2-i
                else:
                    count+=i-2
                if(j<=2):
                    count+=2-j
                else:
                    count+=j-2   
                print(count)     
                        	     
                
                   