#10. [Find All Numbers Disappeared in an Array](https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/) leetcode
def findDisappearedNumbers( nums):
            set_of_nums = set(nums)    
            x=[] 
            for i in range(1, len(nums) + 1):
                if i not in set_of_nums:
                    x.append(i)

            return x