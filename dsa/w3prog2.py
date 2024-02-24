def sumsquare(l):
    evenSum,oddSum=0,0
    for i in l:
        if(i%2==0):
            evenSum+=(i**2)
        else:
            oddSum+=(i**2)
    oddEvenLst=[oddSum,evenSum]   
    return(oddEvenLst)
print(sumsquare([-1,-2,3,7]))     
