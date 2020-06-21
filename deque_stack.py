# other implementations of stack as 'deque' and 'lifoqueue'
from collections import deque
q = deque()
  
q.append('eat')
q.append('sleep')
q.append('code')
print(q)
q.pop()
q.pop()
q.pop()
try:
    q.pop()

except:
    print("error")
