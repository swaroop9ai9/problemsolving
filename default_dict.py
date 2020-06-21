# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

n,m=list(map(int,input().split()))
A,B=defaultdict(list),defaultdict(list)
[A[input()].append(i+1) for i in range(n)]
for i in range(m):
    k = input()
    B[k].append(i+1)
for i in B.keys():
    if i in A.keys():
        print(" ".join(map(str,A[i])))
    else:
        print("-1")

