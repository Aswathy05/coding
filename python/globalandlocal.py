#global d is used to change the variable outside the scope of it(outside the function)
#outside d is global scope and inside d is local scope
d=11
def summa():
    global d
    print(d)
summa()    
print(d)

d=10
def summa():
    global d
    print(d)
summa()    
print(d)

d=10
def summa():
    d=5
    print(d)
summa()
print(d)

