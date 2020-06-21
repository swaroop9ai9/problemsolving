# Implemetation of a stack, usually we implement stack using array's or linkedlists.
# Stack follows a LIFO(Last In First Out) principle.
# Implementation of stack has, push(), pop() operations.
# Charecteristics:
#   1) Insertion order is preserved.
#   2) Useful for parsing the operationg
#   3) Duplicacy is allowed

# Class for stack using list
class Stack:
     def __str__(self):
         return str(self.__dict__)
         
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)
        
d = Stack()
print(d.isEmpty())
d.push('Python')
d.push('Java')
d.push('C++')
print(d.peek()) # peek() returns the top element in the list
print(d) # Internally class the __str__ magic method to print the items in stack as dictionary
print(d.pop())
print(d)
print(d.peek())



