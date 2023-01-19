# Jump Game(https://leetcode.com/problems/jump-game/)


nums = [1,3,1,1,4]
goal=len(nums)-1

for i in range(len(nums)-1,-1,-1):
    if i+nums[i]>=goal:
        goal=i
if goal==0:
    print(True)  
else:
    print(False)          
  