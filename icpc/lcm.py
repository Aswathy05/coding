import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

n=int(input())
x=input().split()
s=[]
for i in x:    
    s.append(int(i))
count=0    
for j in range(len(s)):
    for i in range(j):
        maxi=max(s[i],s[j])
        mini=min(s[i],s[j])
        if(maxi%mini==0):
            count+=1
print(count)            

            









""" lcm
i=max(a,b)
while(True):
    if(i%a==0 and i%b==0):
        break 
    i+=1"""