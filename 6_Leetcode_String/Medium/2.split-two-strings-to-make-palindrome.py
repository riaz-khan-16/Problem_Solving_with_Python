

#problem Link:   [Split Two Strings to Make Palindrome](https://leetcode.com/problems/split-two-strings-to-make-palindrome/)

#Take help from Youtube:

#Solution:

#Brute Force Method



a = "x"
b = "y"


a ="abdef"
b ="fecab"

def splitin(word,index):
    pre=word[0:index]
    suff=word[index:len(word)]
    return pre,suff

def isPalindrome(word):
    x=word
    y=word[::-1]
    if x==y:
        return True
    else:
        return False

def check(a,b):
    for i in range(len(a)):
        a1,a2=splitin(a,i)
        b1,b2=splitin(b,i)
        m=a1+b2
        n=b1+a2
        if isPalindrome(m) or isPalindrome(n):
            return True
        
    return False


#Optimizing

def check1(a,b):

    i=0
    j=len(a)-1
    while i>=j:
        a1,a2=splitin(a,i)
        b1,b2=splitin(b,i)
        m=a1+b2
        n=b1+a2
        if isPalindrome(m) or isPalindrome(n):
            return True
        

b ="fecab"   
a ="abdef"



def check(s1,s2):
        n=len(a)
        l=0
        r=n-1
        while l<=r and s1[l]==s2[r]:
            l+=1
            r-=1
        
        if l>r or s1[l:r+1]==s1[l:r+1][::-1] or s2[l:r+1]==s2[l:r+1][::-1]:
            return True
        return False
print(check(a,b) or check(b,a))











