#  [Sort Colors](https://leetcode.com/problems/sort-colors/)

nums = [2,0,2,1,1,0]

zero=nums.count(0)
one=nums.count(1)
two=nums.count(2)
for x in range(len(nums)):
    if two:
        nums.pop()
        nums.insert(0,2)
        two-=1
    elif one:
        nums.pop()
        nums.insert(0,1)
        one-=1
    else:
        nums.pop()
        nums.insert(0,0)
print(nums)        
        
         

# alternative         

# red, white, blue = 0, 0, len(nums)-1
    
#     while white <= blue:
#         if nums[white] == 0:
#             nums[red], nums[white] = nums[white], nums[red]
#             white += 1
#             red += 1
#         elif nums[white] == 1:
#             white += 1
#         else:
#             nums[white], nums[blue] = nums[blue], nums[white]
#             blue -= 1
      

