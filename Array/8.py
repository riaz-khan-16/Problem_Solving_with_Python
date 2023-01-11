#How Many Numbers Are Smaller Than the Current Number


# Given the array nums, for each nums[i] find out how many numbers in
#  the array are smaller than it. That is, for each nums[i] you have to count
#  the number of valid j's such that j != i and nums[j] < nums[i].

# Return the answer in an array.


# Input: nums = [8,1,2,2,3]
# Output: [4,0,1,1,3]

nums = [8,1,2,2,3]
arr=[]
for i in range(len(nums)):
    a=0
    
    for j in range(len(nums)):
            if nums[i]>nums[j]:
                a=a+1
    arr.append(a)  
print(arr)             