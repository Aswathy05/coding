import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
t=int(input())
for i in range(t):
    x,y,z=(int(i) for i in input().split())
    avg=(x+y+z)/3
    if(avg<30):
        print("FAIL")
    else:
        print("PASS")    

