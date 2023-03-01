# 14. [Implement strStr()](https://leetcode.com/problems/implement-strstr/)
# Google Interview

haystack = "lopjgsadbutsa"
needle = "sad"


if needle not in haystack:
        print(-1)

for i in range(len(haystack)-len(needle)+1):
    if haystack[i]==needle[0]:
        if haystack[i:i+len(needle)]==needle[0:len(needle)]:
            print(i)

    
# Help taken from:    
#https://www.youtube.com/watch?v=OWaZ6AosS30    



