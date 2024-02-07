#B's current score and target score is inputed, score needed to win is to be found
T=int(input())
for i in range(T):
    a=input()
    lst=a.split()
    x=int(lst[0])
    y=int(lst[1])
    score=x-y
    print(score)