# 6. [Design circular Queue](https://leetcode.com/problems/design-circular-queue/) leetcode

queue=[]
k=3

def enQueue(value):
        """
        :type value: int
        :rtype: bool
        """
        if len(queue)<k:
           queue.append(value)
           return True
        else:
               return False   

def deQueue():
        """
        :rtype: bool
        """
        if queue:
               queue.pop(0)
               return True
        else:
               return False       
        

def Front():
        """
        :rtype: int
        """
        if queue:
               return queue[0]
        else:
               return -1
        

        

def Rear():
        """
        :rtype: int
        """
        if queue:
               return queue[-1]
        else:
               return -1


        

def isEmpty():
        """
        :rtype: bool
        """

        if  not queue:
           return True
        else:
           return False     
          
        

def isFull():
        """
        :rtype: bool
        """

        if len(queue)==k:
               return True
        else:
               return False
        
