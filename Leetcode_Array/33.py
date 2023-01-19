#
#238. Product of Array Except Self
#https://leetcode.com/problems/product-of-array-except-self/


nums=[-1,1,0,-3,3]


prefix=[]
j=1
for i in range(len(nums)):
    j=j*nums[i]
    prefix.append(j)


postfix=[]
k=1
for i in range(len(nums)-1,-1,-1):
    k=k*nums[i]
    postfix.append(k)
postfix.reverse()



an=[]
po=1
pre=1
for i in range(len(nums)):
      
      if i<(len(nums)-1) and i>=1:
        po=postfix[i+1]
        pre=prefix[i-1] 
      elif i>=(len(nums)-1):
        po=1
        pre=prefix[i-1]

      elif i<1:
        pre=1  
        po=postfix[i+1]

      an.append(pre*po)
    
        
print(an)       






