#problem Link:  5. [Repeated String Match](https://leetcode.com/problems/repeated-string-match/)

#Take help from Youtube:

#Solution:


a = "abcd"
b = "cdabcdab"

# a ="aa"
# b ="a"
   
    

def repeatedStringMatch(a, b):
        counter = 1
        tmp = a
        while (len(a)<len(b)):
            a+=tmp
            counter+=1
        if b in a:
            return counter
        if b in a+tmp:
            return counter+1
        return -1

print(repeatedStringMatch(a, b))