# https://leetcode.com/problems/set-mismatch/


# Input: nums = [1,2,2,4]
# Output: [2,3]


def findErrorNums(nums):
        n = len(nums)
        b = sum(nums)
        c = sum(set(nums))
        a = (n * (n+1)) // 2
        missing = a - c
        duplicate = b - c
        return [duplicate, missing]

# n – number of elements in nums
# a – the sum of the correct sequence 1+2+3+4
# b – the sum of nums (sequence w/ duplicate) 1+2+2+4
# c – the sum of set(nums) (sequence w/o duplicate) 1+2+4

# duplicate = b-c – (1+2+2+4) - (1+2+4) = 2
# missing = a-c – (1+2+3+4) - (1+2+4) = 3

