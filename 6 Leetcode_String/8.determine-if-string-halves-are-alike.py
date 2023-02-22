# 8. [Determine if string halves are alike](https://leetcode.com/problems/determine-if-string-halves-are-alike/)

s = "lbolkfdjkook"
n=len(s)//2
a=s[:n]
b=s[n:]

v=['a','e','o','i','u','A','E','O','I','U']
ca=0
cb=0
for i in range(n):
    if a[i] in v:
        ca=ca+1
    if b[i] in v:
        cb=cb+1    

if ca==cb:
    print(True)
else:    
   print(False)