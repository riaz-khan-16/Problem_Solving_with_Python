#21. Two Sum  https://leetcode.com/problems/two-sum/
nums = [3,3]
target = 6

for i in range(len(nums)):
           a=nums[i]
           for j in range(i+1,len(nums)):
                b=a+nums[j]
                if b==target:
                    print(i,j)
