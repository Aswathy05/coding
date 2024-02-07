n=int(input())
if(n>=0):
    print(n)
else:
    num1=list(str(n))
    if(int(num1[len(num1)-1])>=int(num1[len(num1)-2])):
        del num1[len(num1)-1]
    else:
        del num1[len(num1)-2]
    str=""    
    for i in num1:
        str+=i    
    print(int(str))