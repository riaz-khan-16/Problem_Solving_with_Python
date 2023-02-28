# 21. [Merge Strings Alternately](https://leetcode.com/problems/merge-strings-alternately/)

# method-1: brute force

word1 = "abc"
word2 = "pqrr"

         
x=[]
for i in range(len(word1)):
    x.append(word1[i])
    x.append(word2[i])
# print(''.join(x))    



# method-2: 
word1 = "abc"
word2 = "pqrkkkkkkkkkkkkkkkkkkkkk"
len_word1=len(word1)
len_word2=len(word2)

i=0
j=0
k=''
while i<len_word1 or j<len_word2:

    if i<len_word1:
        k=k+word1[i]
        i=i+1
    if j<len_word2:
       k=k+word2[j]
       j=j+1

# method-3: 



def mergeAlternately(word1, word2):
        
        res=''
        
        for i in range(min(len(word1),len(word2))):
            res += word1[i] + word2[i]
            
        return res + word1[i+1:] + word2[i+1:]


