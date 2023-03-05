#https://leetcode.com/problems/height-checker/


# Input: heights = [1,1,4,2,1,3]
# Output: 3
# Explanation: 
# heights:  [1,1,4,2,1,3]
# expected: [1,1,1,2,3,4]
# Indices 2, 4, and 5 do not match.

heights = [1,1,4,2,1,3]

expected=sorted(heights)

nm=0
print(expected)

for i in range(len(heights)):
    if heights[i]!=expected[i]:
        nm=nm+1

print(nm)


