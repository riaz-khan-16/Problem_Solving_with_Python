
# Minimum Cost to Move Chips to The Same Position
# https://leetcode.com/problems/minimum-cost-to-move-chips-to-the-same-position/



position =[6,4,7,8,2,10,2,7,9,7]


a=position
o=0
e=0
for i in a:
        #find even po
      if  i%2!=0:
        o=o+1
      else:
        e=e+1  
print (min((e,o)))         




