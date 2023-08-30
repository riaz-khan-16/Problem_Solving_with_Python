# # 3. [Middle of the Linked List](https://leetcode.com/problems/middle-of-the-linked-list/) leetcode


# # Algorithm
# #  1. Find the  length of the list
# #  2. find half of the list
# #  3. if there is two middle select the second
# #  4.find that position node

     
     

class Listnode:
    def __init__(self,val,next=None):
        self.val=val
        self.next=next

def print_list(head):
    current_node= head
    while current_node:
        print(current_node.val)
        current_node=current_node.next

def find_middle_position(head):
        currentNode=head
        length=0
        while currentNode is not None:
            currentNode=currentNode.next
            length=length+1
        
        if length%2==1:
             mposition=length//2
            
             return mposition
        else:
             mposition=length/2 
            
             return mposition   
        
def find_middle_node(head,mpositon):
     current_node=head
     current_pos=0
     while True:
          if current_pos==mpositon:
               print(current_node.val)
               return current_node
          current_node=current_node.next
          current_pos=current_pos+1
          
          


           
n7=Listnode(7)
n6=Listnode(6,n7)
n5=Listnode(5,n6)     
n4=Listnode(4,n5)  
n3=Listnode(3,n4)
n2=Listnode(2,n3)    
n1=Listnode(1,n2) 
print_list(n1)
x=find_middle_position(n1)
find_middle_node(n1,x)
            
