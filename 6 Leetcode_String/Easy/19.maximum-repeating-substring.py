# 19. [Maximum Repeating Substring](https://leetcode.com/problems/maximum-repeating-substring/)


sequence = "ababc"
word = "ab"

def maxRepeating(self, sequence: str, word: str) -> int:
        if len(sequence) < len(word):
            return 0
        ans = 0
        k = 1
        while word*k in sequence:
            ans += 1
            k += 1
        return ans