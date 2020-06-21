# Implementation of queue
# Operations associated with queue are
#   1) Enqueue: Adds an item to the queue, if queue is full is will overflow
#   2) Dequeue: Removes an item from the queue. The items are popped in the same order
#   3) Front: gets the front item in the queue
#   4) Rear: gets the last item from the queue

# We can implement the queue via:
#   1) List
#   2) Collections.deque
#   3) queue.Queue

print("Implementation using Lists")
queue=[]
#adding elements to the queue
queue.append('a')
queue.append('b')
queue.append('c')
print('Initial queue')
print(queue)

#removing elements from the queue
print("\n Elements dequeued from the queue")
print(queue.pop(0))
print(queue.pop(0))

print("Queue after removing elements")
print(queue)

#Implementation using deque

print("Implementation using dequeue")
from collections import deque
L = deque()

#Data is inserted in 'L' at the end using append()
L.append(9)
L.append(6)
L.append(7)
print("initial queue using deque")
#Removing elements from a deque
print("\n Elements dequeued from the queue")
print(L.popleft())
print(L.popleft())
print("\n queue after removing elements")
print(L)

# Implementation using queue.Queue
# Is a built-in module of python which is used to implement a queue
# queue.Queue(maxsize) initializes a variable to a maximum of maxsize

# get() takes data from the head of the queue
from queue import Queue
L=Queue(maxsize=3)
L.put('a')
L.put('b')
L.put('c')
print("Initial queue",L)
print("\n Elements dequeued from the queue")
print(L.get())
print(L.get())
print(L.get())
print("\n Empty ?",q.empty())

