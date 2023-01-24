#[Find #Smallest Letter Greater Than Target]
#(https://leetcode.com/problems/find-smallest-letter-greater-than-target/)


# You are given an array of characters letters that is sorted in non-decreasing order, and a character target.
#  There are at least two different characters in letters.

# Return the smallest character in letters that is lexicographically greater than target. 
# If such a character does not exist, return the first character in letters.

 

# Example 1:

# Input: letters = ["c","f","j"], target = "a"
# Output: "c"
# Explanation: The smallest character that is lexicographically greater than 'a' in letters is 'c'.


class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        mn=letters[0]
        for i in letters:
             if i>target:
                 return i
        return mn  

#This code will work in the leetcode     