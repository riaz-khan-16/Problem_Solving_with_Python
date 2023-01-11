# Check if the Sentence Is Pangram leetcode-1832


# A pangram is a sentence where every letter of the English alphabet appears at least once.

# Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.
# Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
# Output: true
# Explanation: sentence contains at least one of every letter of the English alphabet.

a=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
sentence = "thequickbrownfoxjumpsoverthelazydog"
sentenceInArray=[]
for k in sentence:
      sentenceInArray.append(k)
    
for i in a:
    if i not in sentenceInArray:
        print('No') 
print('yeah')   


