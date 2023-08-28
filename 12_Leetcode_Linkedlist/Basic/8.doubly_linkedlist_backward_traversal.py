# Doubly Linkedlist Traversal Backward


class  Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class Dll:
    def __init__(self):
        self.head=None
    def backward_traversal(self):
        if self.head is None:
            print("Emptylinkedlist") 
        last=self.head
         
        while last.next is not None:
            last=last.next
        a=last
        while a is not None:
            print(a.data)
            a=a.prev

        
    


n1=Node(5)
dll=Dll()
dll.head=n1
n2=Node(10)
n2.prev=n1
n1.next=n2
n3=Node(15)
n2.next=n3
n3.prev=n2

dll.backward_traversal()