# 2. [Shuffle String](https://leetcode.com/problems/shuffle-string/)


# 1528. Shuffle String


s = "codeleet"
indices = [4,5,6,7,0,2,1,3]

res = ['']*len(s)


for i in range(len(s)):

    res[indices[i]] = s[i]

res=''.join(res)
print(res)
    
