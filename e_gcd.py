def egcd(m,n):
    #Assume m>n
    if n>m:
        (m,n)=(n,m)
    if m%n==0:
        return str(n)
    else:
        diff=m-n
        return(egcd(max(n,diff),min(n,diff)))

print(egcd(int(input('Number 1\n')),int(input('Number 2\n'))))
