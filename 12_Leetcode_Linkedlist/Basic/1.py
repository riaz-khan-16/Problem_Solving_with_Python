class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Linkedlist:
    def __init__(self):
        self.head=None

    def  insert(self,newNode):
        if self.head is None:
            self.head=newNode
        else:
            #find the last node
            lastNode=self.head
            while True:
                if lastNode.next is None:
                    break
                lastNode=lastNode.next
            lastNode.next=newNode

    def printNode(self):
        currentNode=self.head
        while True:
            if currentNode is None:
                break
            print(currentNode.data)    
            currentNode=currentNode.next


firtsnode=Node("Riaz")
x=Linkedlist()
x.insert(firtsnode)
secondnode=Node('galib')
x.insert(secondnode)
secondnode1=Node('ga1lib')
x.insert(secondnode1)
x.printNode()



     