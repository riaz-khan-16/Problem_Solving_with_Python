# alternative way for 36
nums = [1,2,3,4,5,6,7] 
k = 3
if k == 0:
    print(nums)
        
# # compute rotation
k = k % len(nums)
lenght = len(nums)

# #swap positions
nums[lenght-k:], nums[:lenght-k] = nums[:lenght-k],nums[lenght-k:]
print(nums)

