# 12. [Reverse Words in a String III](https://leetcode.com/problems/reverse-words-in-a-string-iii/)


s = "Let's take LeetCode contest"

s=s.split(' ')
print(s)
for i in range(len(s)):
    x=s[i]
    s[i]=x[::-1]
print(' '.join(s))    

    
