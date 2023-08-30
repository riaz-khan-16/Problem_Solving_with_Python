#4. [Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/) leetcode

#algorithm

# 1. make two list
# 2.make a empty merged list


class Listnode:
    def  __init__(self,val=0,next=None):
        self.val=val
        self.next=next
def print_list(head):
    current_node= head
    while current_node:
        print(current_node.val)
        current_node=current_node.next

l1=Listnode(1)
l1.next=Listnode(2)
l1.next.next=Listnode(3)    

l2=Listnode(1)
l2.next=Listnode(3)
l2.next.next=Listnode(5)  

merged=Listnode()
current=merged
while l1 and l2:
   if l1.val<l2.val:
       current.next=l1
       l1=l1.next
   else:
       current.next=l2
       l2=l2.next
   current=current.next
if l1:
    current.next=l1
if l2:
    current.next=l2

print_list(merged.next)                       

       









