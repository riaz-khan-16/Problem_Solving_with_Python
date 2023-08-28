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
    
    def insert_begining(self,new_node):
        a=self.head
        a.prev=new_node
        new_node.next=a
        self.head=new_node
    def forward_traversal(self):
        if self.head is None:
            print("Emptylinkedlist")   
        else:
            a=self.head
            while a is not None:
                print(a.data)
                a=a.next

    def insertion_at_end(self,new_node):
         #find last node
         last=self.head
         while last.next is not None:
             last=last.next
         last.next=new_node
         new_node.prev=last  

         
    


n1=Node(5)
dll=Dll()
dll.head=n1
n2=Node(10)
n2.prev=n1
n1.next=n2
n3=Node(15)
n2.next=n3
n3.prev=n2

n4=Node(20)

n5=Node(25)



# dll.backward_traversal()
# dll.insert_begining(n4)
dll.insertion_at_end(n5)

dll.forward_traversal()
