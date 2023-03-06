#problem Link:   4. [Sentence Similarity III](https://leetcode.com/problems/sentence-similarity-iii/)

#Take help from Youtube:

#Solution:
sentence1 = "My name is Haley"
sentence2 = "My Haley"

#Method 1



 


def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        s1 = sentence1.split()
        s2 = sentence2.split()
        if(len(s1)>len(s2)):            #let s1 be the smaller and s2 be the greater
            s1,s2 = s2,s1
        while(s1): 
            if(s2[0]==s1[0]):
                s2.pop(0)
                s1.pop(0)
            elif(s2[-1]==s1[-1]):
                s2.pop()
                s1.pop()
            else:
                return(False)            
        return(True)




        

       


          

# find large sentence and smaller sentence

