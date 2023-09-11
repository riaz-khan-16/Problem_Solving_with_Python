# 6. [Number of Recent Calls](https://leetcode.com/problems/number-of-recent-calls/) leetcode
class RecentCounter(object):

    def __init__(self):
        self.requests=[]
        

    def ping(self, t):
        """
        :type t: int
        :rtype: int

        """ 
        x=self.requests
        x.append(t)
        
        while x and x[0] < t - 3000:
            x.pop(0)

        return len(x)