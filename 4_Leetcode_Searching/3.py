# https://leetcode.com/problems/first-bad-version/
# 278. First Bad Version

# n = 10 
# bad = 4


# start=0
# end=n
# while start+1<end:
#     mid=(start+end)//2
#     if isBadVersion(mid): #builtinf function
#         end=mid
#     else:
#         start= mid
# return end