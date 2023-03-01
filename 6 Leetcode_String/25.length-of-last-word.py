# 25. [Length of last word](https://leetcode.com/problems/length-of-last-word/)

s = "   fly me   to   the moon  "
s=s.lstrip(' ').rstrip(' ')
s=s.split(' ')

print (len(s[-1]))
print(s)
