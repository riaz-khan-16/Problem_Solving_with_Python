#16. [Count the Number of Consistent Strings](https://leetcode.com/problems/count-the-number-of-consistent-strings/)


allowed = "ab"
words = ["ad","bd","aaab","baa","badab"]

def countConsistentStrings(allowed,words):
        allowed = set(allowed)
        count = 0
        
        for word in words:
            for letter in word:
                if letter not in allowed:
                    count += 1
                    break
        
        return len(words) - count