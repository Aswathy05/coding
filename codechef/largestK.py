for i in range(int(input())):
    x,y=(int(i) for i in input().split())
    if(y//2<x//2):
        print(0)
    else:
        print(y//(x-1))    