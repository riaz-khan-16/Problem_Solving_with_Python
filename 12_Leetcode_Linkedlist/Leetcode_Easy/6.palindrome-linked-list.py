#6. [Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list/) leetcode Snapdeal

#chat gpt
        
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def isPalindrome(head):
    # Step 1: Find the length of the linked list
    length = 0
    current = head
    while current:
        length += 1
        current = current.next
    print(length)
    # Step 2: Split the linked list into two halves
    first_half_end = head
    for _ in range(length // 2):
        first_half_end = first_half_end.next
    print(first_half_end.val)
    # Step 3: Reverse the second half
    prev = None
    current = first_half_end.next
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    second_half_start = prev
    print(second_half_start.val)
    # Step 4: Compare the two halves
    current1 = head
    current2 = second_half_start
    while current2:
        if current1.val != current2.val:
            return False
        current1 = current1.next
        current2 = current2.next
    return True

def print_list(head):
    current_node= head
    while current_node:
        print(current_node.val)
        current_node=current_node.next

head=ListNode(1)
head.next=ListNode(2)
print_list(head)


        