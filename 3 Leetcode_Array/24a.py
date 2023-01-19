nums=[-1,-3,5,-1]

Sum = 0
maxi = nums[0]
for ele in nums:
   Sum = Sum+ele
   if maxi<Sum:
     maxi = Sum
   if Sum<0:
    Sum = 0
print(maxi)    

           

    