# 2. [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) leetcode
# head=[1,2,3,4,5]
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def printNode(self,head):
        currentNode=head
        while True:
            if currentNode is None:
                
                break  
            print(currentNode.val)
            currentNode=currentNode.next

def  reverse(head):
        current=head
        prev=None
        while current:
            temp=current.next
            current.next=prev
            prev=current
            current=temp
        return prev


n5=ListNode(5)
n4=ListNode(4,n5)
n3=ListNode(3,n4)
n2=ListNode(2,n3)
n1=ListNode(1,n2)
x=ListNode()
print("before:")
x.printNode(n1)

print("after")
r=reverse(n1)
x.printNode(r)




