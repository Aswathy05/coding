#Quicksort
def find_median(list):
    n=len(list)
    start,mid,end=list[0],list[n//2],list[n-1]
    L=[start,mid,end]
    if start>mid:
        L[0],L[1]=L[1],L[0]
    if mid>end:
        L[2],L[1]=L[1],L[2]
    if start>end:
        L[1],L[2]=L[2],L[1]
    return L[2]
def partition(list,begin,end):
    pivot=find_median(list)
    i=begin
    j=end-1
    while i<=j:
        while list[i]<=pivot and i <end:
            i+=1
        while list[j]>pivot and j>=begin:
            j=j-1
        
        if i<j:
            list[i],list[j]=list[j],list[i]
            i+=1
            j-=1
    if i<end:
         list[i],list[end]=list[end],list[i]
    return i
    
def quicksort(list,begin,end):
    if begin<end:
        k=partition(list,begin,end)
        quicksort(list,begin,k-1)
        quicksort(list,k+1,end)
        return list
    
a=[2,33,4,1,-2,3]
print(quicksort(a,0,len(a)-1))
print(a)