#Concatenation of Array(Leetcode-1929)


# Input: nums = [1,2,1]
# Output: [1,2,1,1,2,1]

nums = [1,2,1]
def getConcatenation():
    ans=nums+nums
    return ans

print(getConcatenation())