# https://leetcode.com/problems/3sum/

# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
# such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

 

# Example 1:

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]



nums = [-1,0,1,2,-1,-4]

# Algorithm:
#            1.Sort the list.  
#            2.Apply a for loop and take every number:

#                    i)     the first number is ---> 1st =nums[i]
#                    ii)    Now we will check every remaining element as 2nd and 3rd number:
#                                             2nd=nums[i+1], 3rd=nums[len(nums)-1]
#                    iii)   Sum = 1st + 2nd + 3rd
#                    iv)    if Sum == 0 add this to an empty array---r
#                    v)     if no combination found exit the loop and go back to the for loop
#                    vi)    1st = nums[i] ( if num[i-1]!=num[i])

#            3. Return the array r
#
                      
def threeSum(nums):
    res = []
    nums.sort()
    for i in range(len(nums)-2):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        l, r = i+1, len(nums)-1
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if s < 0:
                l +=1 
            elif s > 0:
                r -= 1
            else:           
                res.append((nums[i], nums[l], nums[r]))
                while l < r and nums[l] == nums[l+1]:
                    l += 1
                while l < r and nums[r] == nums[r-1]:
                    r -= 1
                l += 1; r -= 1
    return res

def threeSumRiaz(nums):  
     nums.sort()
     r=[]
     l=len(nums)-1
     for i in range(l-1):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        a=i
        # now apply two pointer method
        b=i+1
        c=l
        while b<c:
            sum= nums[a]+nums[b]+nums[c]
            
            if sum>0:
                c=c-1
            elif sum<0:
                 b=b+1
            else:
                r.append([nums[a],nums[b],nums[c]])  
                while b<c and nums[b]==nums[b+1]:
                      b=b+1
                while b<c and nums[c]==nums[c-1]:
                      c=c-1      

                b=b+1
                c=c-1
     return r  

print(threeSumRiaz(nums))














    
                                                     

                                  