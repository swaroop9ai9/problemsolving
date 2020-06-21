#namedtuple application for average marks.
from collections import namedtuple

(n, categories) = (int(input()), input().split())
Grade = namedtuple('Grade', categories)
#marks = [int(Grade._make(input().split()).MARKS) for _ in range(n)]
ls = list()
for _ in range(n):
    k=Grade._make(input().split())
    ls.append(int(k.MARKS))
#print(ls)
print((sum(ls) / int(n)))
