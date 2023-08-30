# 5. [Delete Node in a Linked List](https://leetcode.com/problems/delete-node-in-a-linked-list/) leetcode


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteNode(node):
    # Copy the value of the next node to the current node
    node.val = node.next.val
    # Update the next pointer to skip the next node
    node.next = node.next.next
