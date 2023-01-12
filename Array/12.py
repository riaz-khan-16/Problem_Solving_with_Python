#Leetcode:1732. Find the Highest Altitude


gain = [-5,1,5,0,-7]

a=[0]
b=0
for i in range(len(gain)):
       
       b=b+gain[i]
       a.append(b)

print(max(a))       