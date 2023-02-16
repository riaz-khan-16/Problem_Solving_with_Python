# [Group Anagrams](https://leetcode.com/problems/group-anagrams/)


# Given an array of strings strs, group the anagrams together. 
# You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically
#  using all the original letters exactly once.



# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]


#Algorithm:
          # make a method that take an string and returns array
          # make a method that take two array a,b and checks equal or not
          # make a method that take True/False and if true it will at an element in a array

# string  to array
str='abc'
def  string_to_array(str):
      arr=[]
      for i in str:
        arr.append(i)
      return arr  



def checks_equal_or_not(a,b):
  if len(a)==len(b):  
    m=set(a)
    for i in m:
        if a.count(i)==b.count(i):
            continue
        else:
            return False
    return True    
  else:
    return False         


   
# def   checks_equal_or_not(a,b):
#     if len(a)==len(b):
#        for i in range(len(a)):
#             if a[i] in b:
#                 continue
#             else:
#                 return False
#        return True 
#     else:
#         return False     

x=["eat","tea","tan","ate","nat","bat"]
x=["ddddddddddg","dgggggggggg"]
x=["","b"]
d=[]
e=[]
for i in range(len(x)):
  
 if x[i] not in e: 
    c=[x[i]]
    for j in range(i+1,len(x)):
        a=x[i]
        b=x[j]

        if checks_equal_or_not(a,b):
             c.append(b)
             e.append(b)
             e.append(a)
             
    d.append(c)


  

    


print(d)


x='aaab'
print(set(x))



    






