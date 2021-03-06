class Node:
    def __init__(self,value):
        self.left=None
        self.right=None
        self.value=value

class BinarySearchTree:
    def __init__(self):
        self.root =None

    def insert(self,value):
        new_node=Node(value)
        if self.root==None:
            self.root=new_node
        else:
            temp=self.root
            while(True):
                if new_node.value>temp.value:
                    if temp.right==None:
                        temp.right=new_node
                        return
                    temp = temp.right
                elif new_node.value<temp.value:
                    if temp.left==None:
                        temp.left=new_node
                        return
                    temp=temp.left
    def lookup(self,value):
        if self.root==None:
            return False
        temp = self.root
        while(temp):
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            elif value == temp.value:
                if temp.left==None and temp.right==None:
                    return temp.value,"left Node:None",'Right Node:None'
                elif temp.left!=None and temp.right!=None:
                    return temp.value,temp.left.value,temp.right.value
                elif temp.left==None and temp.left!=None:
                    return temp.value,print("Left Node:None"),temp.left.value
                elif temp.left!=None and temp.right==None:
                    return temp.value,temp.left.value,"Right Node:None"
        return False

    def print_trees(self,round=0):
        round=round+1
        if self.root !=None:
            self.printt(self.root)
        print(round)
    def printt(self,curr_node):
        if curr_node !=None:
            self.printt(curr_node.left)
            # print(str(curr_node.value))
            self.printt(curr_node.right)


   




    # def remove(self):
tree = BinarySearchTree()
tree.insert(9)
tree.insert(4)
tree.insert(6)
tree.insert(20)
tree.insert(170)
tree.insert(15)
tree.insert(1)
v2=tree.lookup(9)
print(v2)


