class Node():
    def __init__(self,data):
        self.data = data
        self.next =None

class LinkedList():

    def __init__(self):
        self.head = None
        self.tail = None


    def append(self,value):
      new_node =Node(value)
      if self.head==None:
          self.head =new_node
          self.tail =new_node
          self.length =1
      else:
          self.tail.next =new_node
          self.tail = new_node
          self.length +=1

    def prepend(self,value):
        new_node =Node(value)
        if self.head ==None:
            self.head =new_node
            self.tail =new_node
            self.length =1
        else:
            new_node.next = self.head
            self.head = new_node
            self.length +=1

    def insert(self,index,data):
        new_node = Node(data)
        temp = self.head
        if index>self.length:
            self.append(data)
            return
        if index==0:
            self.prepend(data)
            return
        else:
            new_node = Node(data)
            temp = self.head
            for x in range(index - 1):
                temp = temp.next
            a = temp.next
            new_node.next = a
            temp.next = new_node
            self.length += 1

    def remove(self,index):
        if index==0:
            temp=self.head
            b=temp.next
            self.head=b
            temp.next=None
            self.length -=1
        else:
            temp = self.head
            for x in range(index - 1):
                temp = temp.next
            a = temp.next
            b = a.next
            temp.next = b
            self.length -=1


    def printl(self):
        temp =self.head
        while temp!= None:
            print(temp.data,end=' ')
            temp = temp.next
        print()
        print('Length= '+str(self.length))

    def reverse(self):
        if self.head.next==None:
            return self.head
        else:
            first =self.head
            self.tail=self.head
            second =first.next
            while(second!=None):
                temp=second.next
                second.next =first
                first =second
                second = temp
            self.head.next =None
            self.head=first
            return self.printl()



l=LinkedList()

l.append(1)
l.append(2)
l.append(3)
l.append(4)
l.append(5)
l.reverse()

