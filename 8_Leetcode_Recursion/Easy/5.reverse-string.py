# 5. [Reverse String](https://leetcode.com/problems/reverse-string/) leetcode

# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]

a = ["h","e","l","l","o"]

left=0
right=len(a)-1
def rever(a,left,right):
    if left>right:
        return a
    a[left],a[right]=a[right],a[left]
    return rever(a,left+1,right-1)
print(rever(a,left,right))


