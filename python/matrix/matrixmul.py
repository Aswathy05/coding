'''
3 loops:
row of A
col of B
col of A and row of B
'''

A=[[1,2,3],[4,5,6],[7,8,9]] #order=axb
B=[[1,2,3],[4,5,6]]         #order=bxc
sum=0
main_lst=[]
for i in range(len(A)):
    for j in range(len(B[0])):
        lst=[]
        for k in range(len(B)):
            sum+=i*j
        print(sum)
        lst.append(sum)     


