# 18. [Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/)


strs = ["nflower","flow","flight"]

#Algo:
#     1. Learn how to take first prefix of a string
#     2. Learn how to take  1st prefix of a list of string
#     3. Learn how to check all of the 1st prefix are equal or not
#     4. Learn how to check all of the 2nd prefix are equal or not
#     5. Learn how to check all of the 3rd prefix are equal or not
#     6. If 1st prefix is equal for all add it to any variable


def longestCommonPrefix(self, strs):



    def find(strs,j):
        
        for i in strs:
            x=min(strs,key=len)
            x=x[j]
            if i[j]==x:
                continue
            else:
            return False
        return True

    if  "" in  strs:
            return ("") 

    if len(strs)==1:
        return  strs[0]   
    r=[]
    y=min(strs,key=len)
    for j in range(len(y)):
        if find(strs,j):
            r.append(y[j])
        else:
            break
    return (''.join(r))




# collected

def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        shortest = min(strs,key=len)
        for i, ch in enumerate(shortest):
            for other in strs:
                if other[i] != ch:
                    return shortest[:i]
        return shortest 