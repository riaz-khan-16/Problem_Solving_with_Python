# https://leetcode.com/problems/largest-number/


# Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.

# Since the result may be very large, so you need to return a string instead of an integer.

 

# Example 1:

# Input: nums = [10,2]
# Output: "210"
# Example 2:

# Input: nums = [3,30,34,5,9]
# Output: "9534330"


nums = [3,30,34,5,9,100,200,548]

#Algorithm
# 1.make a function that takes two inputs and return their best composition
# 2. apply this comparison for all values
def convertTostr(nums):
    for i in range(len(nums)):
        nums[i]=str(nums[i])
    return nums    

nums=convertTostr(nums)

def findbest(a,b):
    if a+b>b+a:
        return True
    else:
        return False

for i in range(len(nums)):
    for j in range(i+1,len(nums)):
     if not findbest(nums[i],nums[j]):
        nums[j],nums[i]=nums[i],nums[j]

nums=''.join(nums)

nums=nums.lstrip('0')
if not nums:
    print ('0')
else:
   print(nums)
      


# Learn 
# 1. nums.sort(key=lambda x: x*10, reverse=True)
# 2. ''.join(nums)
# 3. lstrip('0')    


# learn it:

        # https://docs.python.org/3/howto/sorting.html 
        # https://www.programiz.com/python-programming/methods/list/sort
        # https://www.w3schools.com/python/ref_string_join.asp
        # https://www.w3schools.com/python/ref_string_lstrip.asp



 

         


