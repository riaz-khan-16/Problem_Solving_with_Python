# 11. [Remove Linked List Elements](https://leetcode.com/problems/remove-linked-list-elements/) leetcode


class ListNode:
    def __init__(self,data=0,next=None):
        self.val=data
        self.next=next


def remove_val(head,val):
    #check weather a node have the value or not
    x=head
    while x.next is not None:
        if x.val==val:
           #delete the node
           x.val = x.next.val
           x.next=x.next.next
           print("deleted")
        else:
            x=x.next
            
               
           











def print_list(head):
    x=head
    while x is not None:
        print(x.val)
        x=x.next


n=ListNode(1)
n.next=ListNode(2)
n.next.next=ListNode(3)
n.next.next.next=ListNode(3)
n.next.next.next.next=ListNode(5)
remove_val(n,3)
print_list(n)



    

