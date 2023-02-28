# 22. [Reverse Prefix of Word](https://leetcode.com/problems/reverse-prefix-of-word/)

#method 1
word = "abcdefd"
ch = "d"

if ch not in word:
     print(word)
def findIndex(word,ch):
    for i in range(len(word)):
        if word[i]==ch:
              return i
i= findIndex(word,ch)     
x=word[:i+1]
y=word[i+1:]
x=x[::-1]
print(x+y)
           
#method 2

def reversePrefix(self, word: str, ch: str) -> str:
        idx=word.find(ch)    
        if idx:
            return word[:idx+1][::-1]+ word[idx+1:]
        return word








