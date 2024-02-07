#Create a list which stores the sum of each of the elements from the two lists
l1 = [10,20,30,40,50]
l2 = [100,200,300,400,500]
sumlst = [l1[i]+l2[i] for i in range(len(l1))]
print(sumlst)