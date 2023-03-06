#problem Link:  6. [Next Greater Element III](https://leetcode.com/problems/next-greater-element-iii/)

#Take help from Youtube: https://www.youtube.com/watch?v=fOeD3CW2c7c

#Solution:

def nextGreaterElement(n):
    def next_permutation(l):
        n = len(l)
        if n <= 1:
            return False
        i = n - 1
        while True:
            j = i
            i -= 1  
            if l[i] < l[j]:
                k = n - 1
                while not (l[i] < l[k]):  
                    k -= 1
                l[i], l[k] = l[k], l[i]
                l[j:] = reversed(l[j:])
                return True
            if i == 0:  
                    l.reverse()
                    return False 

    
    l = list(str(n))
    has_next = next_permutation(l)
    ans = int(''.join(l))
    return ans if has_next and ans < 2 ** 31 else -1