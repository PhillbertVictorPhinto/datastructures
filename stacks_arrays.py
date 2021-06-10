class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Queue:
    def __init__(self):
        self.first=None
        self.last=None
        self.length =0

    def peek(self):
        return self.first.data

    def enqueue(self,data):
        new_node =Node(data)
        if self.length==0:
            self.first =new_node
            self.last =new_node
            self.length +=1
        else:
            a=self.last
            a.next=new_node
            self.last=new_node
            self.length +=1


    def dequeue(self):
        if self.length==0:
            return None
        if self.first==self.last:
            a=self.first
            self.last=None
            self.length =0
            return a.data
        else:
            a = self.first
            self.first = self.first.next
            self.length -= 1
            return a.data

    def printl(self):
        temp =self.first
        while(temp!=None):
            print(temp.data,end=' ')
            temp=temp.next

v =Queue()
v.enqueue('Joy')
w=v.dequeue()
print(w)