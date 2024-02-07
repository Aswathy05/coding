n=int(input())
count1,count2=0,0
for i in range(n):
    op=input()      #X++ or --X
    if(op=="X++" or op=="++X"):
        count1+=1
    elif(op=="--X" or op=="X--"):
        count2-=1
print(count1+count2)            
