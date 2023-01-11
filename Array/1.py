#Build Array from Permutation

# Input: nums = [0,2,1,5,3,4]
# Output: [0,1,2,4,5,3]

nums = [0,2,1,5,3,4]


def BuildArrayfromPermutation():
    ans=[]
    for i in nums:
        ans.append(nums[i])
    return ans    

print(BuildArrayfromPermutation())

