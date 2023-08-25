# 2.How to add new node at the beginning of the list


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
    def insertAt(self,newNode,position):
        currentNode=self.head
        currentPosition=0
        while True:
            if currentPosition==position:
                prevNode.next=newNode
                newNode.next=currentNode
                break
            prevNode=currentNode
            currentNode=currentNode.next
            currentPosition=currentPosition+1



    def insertHead(self,newNode):
        temporary=self.head
        self.head=newNode
        self.head.next=temporary
        del temporary


    def printNode(self):
        currentNode=self.head
        while True:
            if currentNode is None:
                break
            print(currentNode.data)    
            currentNode=currentNode.next


firtsnode=Node("10")
x=Linkedlist()
x.insert(firtsnode)
secondnode=Node('20')
x.insert(secondnode)
secondnode1=Node('30')
x.insert(secondnode1)
fourthnode=Node('0')
x.insertHead(fourthnode)

newnode=Node('15')
x.insertAt(newnode,2)

x.printNode()



     

