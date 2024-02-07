lst=input().split()
n=int(lst[0])   #frends
k=int(lst[1])   #bottles
l=int(lst[2])   #ml of drink
c=int(lst[3])   #Limes
d=int(lst[4])   #lime slices
p=int(lst[5])   #grams of salt
nl=int(lst[6])  #each frnd need nl mls of drink
np=int(lst[7])  #each frnd needs np of salt and a slice lime
toasts=(k*l)//(nl)
limes=c*d
salt=p/np
print(int(min(toasts,limes,salt)//n))