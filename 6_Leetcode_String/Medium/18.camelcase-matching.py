#problem Link:  18. [Camelcase Matching](https://leetcode.com/problems/camelcase-matching/

#Take help from Youtube:

#Solution:


def camelMatch(self, queries, pattern):
        def match(p, q):
            i = 0
            for j, c in enumerate(q):
                if i < len(p) and p[i] == q[j]: i += 1
                elif q[j].isupper(): return False
            return i == len(p)
        
        return [True if match(pattern, s) else False for s in queries]