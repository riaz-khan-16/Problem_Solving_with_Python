#problem Link:  7. [Maximum Number of Removable Characters](https://leetcode.com/problems/maximum-number-of-removable-characters/)


#Take help from Youtube: https://www.youtube.com/watch?v=NMP3nRPyX5g&t=173s
#Solution:



# Make a method to check is p is  a subsequence or not
s = "abcacb"
p = "ab"
removable = [3,1,0]

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

#linear search
x=0
for i in removable:
    s=list(s)
    s.pop(i)
    s.insert(i,' ') 
    s=''.join(s)
    if check_subsequence(s,p):
        x=x+1
print(x)








def maximumRemovals(s,p,removable):
        n = len(removable)
        slen, plen = len(s), len(p)
        
        def is_sub(k):
            arr = set(removable[:k+1])
            i, j = 0, 0
            while i < slen and j < plen:
                if i in arr or s[i] != p[j]:
                    i += 1
                elif s[i] == p[j]:
                    i += 1
                    j += 1
            return j == plen
        
        l, r = 0, n-1
        while l <= r:
            mid = (l+r)>>1
            if is_sub(mid):
                l = mid+1
            else:
                r = mid-1
        return l






 

