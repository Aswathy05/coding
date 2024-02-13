def gcd(m,n):
    if(m<n):
        m,n=n,m
    if(m%n==0):
        return(n)
    else:
        diff=m-n                                #m=ad , n=bd, m-n = ad-bd = (m-n)d , d also divides m-n => gcd(m,n)==gcd(m,m-n)
        return(gcd(max(n,diff),min(n,diff)))    #recursion
print(gcd(12,4))     

#better
def gcd(m,n):
    if(m<n):
        m,n=n,m
    if(m%n==0):
        return(n)
    else:
        return(gcd(n,m%n))