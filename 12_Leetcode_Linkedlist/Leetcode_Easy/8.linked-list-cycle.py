# 8. [Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/) leetcode Samsung
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def hasCycle(head):
    visited = set()
    
    current = head
    
    while current:
        if current in visited:
            return True
        visited.add(current)
        current = current.next
    
    return False
