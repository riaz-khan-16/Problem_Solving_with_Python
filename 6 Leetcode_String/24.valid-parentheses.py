#24. [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)


# Understanding Help : https://www.youtube.com/watch?v=WTzjTskDFMg


s = "([])]"

s = "{}{{}}"



while '()' in s or '[]' in s or '{}' in s:
           s=s.replace('()','').replace('[]','').replace('{}','')
           
             
print(s)