#5. [Sorting the Sentence](https://leetcode.com/problems/sorting-the-sentence/)


s = "is2 sentence4 This1 a3"


s=s.split(' ')


def f(x):
    return x[-1]

s=sorted(s,key=f)   
for i in range(len(s)):
        x=s[i]
        s[i]=x[:-1]
        

print(' '.join(s))