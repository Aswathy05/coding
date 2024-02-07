#factorial using recursive functions
def fact(n):
    if(n<0):
        return None
    elif(n==0):
        return 1
    elif(n==1):
        return 1
    else:
        return n*fact(n-1)

num = input("Enter the number for factorial:")
num = int(num)
ans = fact(num)
if(ans==None):
    print("Not a valid Number")
else:
    print("Factorial=",ans)