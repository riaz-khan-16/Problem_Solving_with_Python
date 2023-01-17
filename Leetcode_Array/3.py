# Running Sum of 1d Array(leetcode-1480)

   

# Input: nums = [1,2,3,4]
# Output: [1,3,6,10]   

nums = [1,2,3,4]
ans=[nums[0]]
def runningSum():
    a=nums[0]
    for i in range(len(nums)-1):
            a=a+nums[i+1]
            ans.append(a)

    return ans
print(runningSum())

