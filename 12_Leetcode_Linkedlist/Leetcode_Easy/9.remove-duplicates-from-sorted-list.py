# 9. [Remove Duplicates from Sorted List](https://leetcode.com/problems/remove-duplicates-from-sorted-list/)leetcode

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteDuplicates(head):
        current = head
        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next

        return head


def print_list(head):
        current_node= head
        while current_node:
            print(current_node.val)
            current_node=current_node.next


n1=ListNode(1)
n2=n1.next=ListNode(1)
n3=n2.next=ListNode(3)
deleteDuplicates(n1)

print_list(n1)

    


