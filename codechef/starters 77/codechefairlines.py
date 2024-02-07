#10 airplanes   find max amt earned on 1st day
t=int(input())
for i in range(t):
    a=input()
    lst=a.split()
    x=int(lst[0])       #capacity of each airplane                          x=2
    y=int(lst[1])       #number of people willing to book in 1 plane        y=15
    z=int(lst[2])       #amt for each ticket    	                        z=10
    if(y<x*10):
        print(y*z)
    else:
        print(x*10*z)    
