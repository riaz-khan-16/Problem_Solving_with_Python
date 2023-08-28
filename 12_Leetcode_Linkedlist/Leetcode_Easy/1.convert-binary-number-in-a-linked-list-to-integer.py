# 1. [Convert Binary Number in a Linked List to Integer]
#(https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/) leetcode


head=[1,0,1]
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def getDecimalValue(head):
        result = 0
        current = head
        
        while current is not None:
            result = (result << 1) + current.val
            current = current.next
        
        return result
n3=ListNode(1)
n2=ListNode(0,n3)
n1=ListNode(1,n2)
decimal_value = getDecimalValue(n1)
print(decimal_value)

