# 3. [Goal Parser Interpretation](https://leetcode.com/problems/goal-parser-interpretation/)


command = "(al)G(al)()()G"

command=command.replace('()','o')

command=command.replace('(','')
command=command.replace(')','')
print(command)
