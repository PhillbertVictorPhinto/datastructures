from collections import deque

class Queue():
    def __init__(self,l):
        self.buffer = deque()
        self.l=l
    def enqueue(self,val):
        self.buffer.appendleft(val)

    def dequeue(self):
        return self.buffer.pop()

    def is_empty(self):
        return  len(self.buffer)==0
    def size(self):
        return(self.buffer)

myqueue1 = Queue(3)
myqueue2 = Queue(3)
for index in range(0,3):
    myqueue1.enqueue(index * 3)
for index in range(0,3):
    if(index==2):
        break
    myqueue2.enqueue(myqueue1.dequeue())

myqueue2.enqueue(12)
print(myqueue1.buffer)
print(myqueue2.buffer)