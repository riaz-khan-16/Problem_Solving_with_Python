# 10. [Number of Strings That Appear as Substrings in Word](https://leetcode.com/problems/number-of-strings-that-appear-as-substrings-in-word/)



patterns = ["a","abc","bc","d"] 
word = "abc"

r=0
for i in patterns:
    if i in word:
        r=r+1
print(r)        
