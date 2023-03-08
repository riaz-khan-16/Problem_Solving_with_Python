# https://leetcode.com/problems/is-subsequence/

s = "acackb"

p = ""


p ="b"
s="abc"
def check_subsequence(main,sub):
    
    if sub=='':
        return True
    j=0
    for i in range(len(main)):
        if main[i]==sub[j]:
            j=j+1
        if j==len(p):
            return True
    return False    

print(check_subsequence(s,p))
