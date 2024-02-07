n=int(input("enter a number:"))
l1=['1','2','3','4','5','6','7','8','9','0']
l2=["one","two","three","four","five","six","seven","eight","nine","zero"]
r=()
for i in str(n):
    x=l1.index(i)
    r+=(l2[x],)
print(r)