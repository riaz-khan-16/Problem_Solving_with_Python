#3. [Min Stack](https://leetcode.com/problems/min-stack/) leetcode


class MinStack(object):

    def __init__(self):
        self.stack=[]
        

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()
        

    def top(self):
        """
        :rtype: int
        """
        x=self.stack
        return x[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        x=self.stack
        return min(x)
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()