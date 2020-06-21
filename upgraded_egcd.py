def up_egcd(m,n):
    #Assume m>n
    if n>m:
        m,n=n,m
    if m%n==0:
        return n
    else:
        return up_egcd(n,m%n)
print(up_egcd(int(input('Number 1\n')),int(input('Number 2\n'))))
