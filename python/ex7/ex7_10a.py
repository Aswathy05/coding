#create a list of integers from the given list

L1 = [1, 'x', 4, 5.6, 'z', 9, 'a', 0, 4]
intlst  = [i for i in L1 if str(i).isdecimal()]
print(intlst)
