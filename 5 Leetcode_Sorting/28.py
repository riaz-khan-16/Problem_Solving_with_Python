# https://leetcode.com/problems/sort-array-by-increasing-frequency/



# 1636. Sort Array by Increasing Frequency
# Given an array of integers nums, sort the array in increasing order based on the frequency of the values. 
# If multiple values have the same frequency, sort them in decreasing order.

# Return the sorted array.

 



# Input: nums = [1,1,2,2,2,3]
# Output: [3,1,1,2,2,2]



# Input: nums = [2,3,1,3,2]
# Output: [1,3,3,2,2]



# Input: nums = [-1,1,-6,4,5,-6,1,4,1]
# Output: [5,-1,4,4,-6,-6,1,1,1]


#algorithm:

#Sort the values in decreasing order
#count frequency of every element
#sort them in ascending order based on the frequency
#if frquency is same put the bigger value first



nums = [2,3,1,3,2]

nums.sort()
nums.reverse()
print(nums)
for i in range(0,len(nums)):
    for j in range(1,len(nums)-i):
            cp=nums.count(nums[j-1])
            cc=nums.count(nums[j])
            if cp>cc:
                #swap
                nums[j-1], nums[j]=nums[j], nums[j-1]

    print(nums)   

print(nums)






