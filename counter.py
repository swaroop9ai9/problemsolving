# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
n = int(input())
ssize = Counter(list(map(int,input().split())))
cus = int(input())
tp=0
for i in range(cus):
    s,pr=list(map(int,input().split()))
    if s in ssize.keys() and ssize[s]>0:
        ssize[s]-=1
        tp+=pr
    else:
        pass

print(tp)

