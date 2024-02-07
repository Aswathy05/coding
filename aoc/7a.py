t=int(input())
cards=["A", "K", "Q", "J", "T", "9", "8", '7', '6', '5', '4', '3', '2']
five=0
four=0
full=0
three=0
two,one,high=0,0,0
for i in range(t):
    hand,bid=input().split()
    elements=set(hand)
    if(len(elements)==5):
        five+=1
    elif(len(elements)==4):
            
