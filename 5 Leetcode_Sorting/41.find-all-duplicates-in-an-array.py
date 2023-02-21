# (https://leetcode.com/problems/find-all-duplicates-in-an-array/

nums = [4,3,2,7,8,2,3,1]

x=[]
for i in nums:
    if nums.count(i)>1:
        x.append(i)
print(set(x))


res = set()
unique = set()
for number in nums:
    if number not in unique:
        unique.add(number)
    else:
        res.add(number)
print(list(res))


#alternative

def findDuplicates(nums):
        res=[]
        for i in nums:
            if nums[abs(i)-1]<0:
                res.append(abs(i))
            else:
                nums[abs(i)-1]=-nums[abs(i)-1]
        return res

           
  




