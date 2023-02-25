# 16. [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/)


s = "A man, a plan, a canal: Panama"
s ="0P"
x=''
for i in s:
    if i.isalnum():
        x=x+i

x=x.lower()
y=x[::-1]

print(x)
if x==y:
    print(True)
else:
    print(False)