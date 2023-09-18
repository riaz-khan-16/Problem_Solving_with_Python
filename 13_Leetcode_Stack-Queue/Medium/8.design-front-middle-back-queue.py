#  8. [Design Front Middle Back Queue](https://leetcode.com/problems/design-front-middle-back-queue/) leetcode
 

queue=[1,2,3,4,5]

def pushFront(val):
        queue.insert(0,val)
        
        

def pushMiddle(val):
        middle=(len(queue)//2)
        queue.insert(middle,val)

               
        

def pushBack(val):
        """
        :type val: int
        :rtype: None
        """
        queue.append(val)
        

def popFront():
        """
        :rtype: int
        """
        queue.pop(0)
        

def popMiddle(self):
        """
        :rtype: int
        """
        middle=(len(queue)//2)-1
        queue.pop(middle)    
        

def popBack():
        """
        :rtype: int
        """
        queue.pop(-1)