def gcd(m,n):
    maxi=1
    for i in range(min(n,m)+1,1):
        if (m%i)==0 and (n%i)==0:
            maxi=i
            break
    return maxi

print(gcd(int(input('Number 1\n')),int(input('Number 2 \n'))))
