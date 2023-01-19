nums = [5,7,7,8,8,8,10]

target = 0
a=[]
if target not in nums:
   print([-1,-1])  
else:  
    for i in range(len(nums)):
        if nums[i]==target:
            a.append(i)
print ([min(a),max(a)])    


 