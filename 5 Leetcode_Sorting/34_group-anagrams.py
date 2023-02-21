#[Group Anagrams](https://leetcode.com/problems/group-anagrams/)


# not done

strs = ["eat","tea","tan","ate","nat","bat"]

words=strs
def group_anagrams(words):
    anagram_groups = {}
    for word in words:
        sorted_word = ''.join(sorted(word))
        if sorted_word in anagram_groups:
            anagram_groups[sorted_word].append(word)
        else:
            anagram_groups[sorted_word] = [word]
    return list(anagram_groups.values())

anagram_groups = {}
for word in words:
        # print(word)
        # print(''.join(sorted(word)))
        sorted_word = ''.join(sorted(word))
        if sorted_word in anagram_groups:
            anagram_groups[sorted_word].append(word)
        else:
            anagram_groups[sorted_word] = [word]
        print(anagram_groups)  


        


        


          

