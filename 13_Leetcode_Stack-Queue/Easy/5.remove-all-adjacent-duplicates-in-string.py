# 5. [Remove All Adjacent Duplicates In String](https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/) leetcode
def removeDuplicates(self, s):
        
        stack=[]
        for i in s:
            if  stack:
                if stack[-1]==i:
                    stack.pop()
                else:
                    stack.append(i)
            else:
                stack.append(i)

        return ''.join(stack)   