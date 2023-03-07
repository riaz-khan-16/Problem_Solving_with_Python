#problem Link:  7. [Maximum Number of Removable Characters](https://leetcode.com/problems/maximum-number-of-removable-characters/)


#Take help from Youtube:
#Solution:

s = "acackb"

p = "abc"

# Make a method to check is p is  a subsequence or not


def removebyindex(string,index):
    string=string[:index]+string[index+1:]
    return string

def removebyelement(string,element):
    for i in range(len(string)):
        if string[i]==element:
            return removebyindex(string,i)
        
def check(mainstring,substring):
    while len(substring)>0:
        x=substring[0]
        substring=removebyindex(mainstring,0)
        if x in mainstring:
            mainstring=removebyelement(mainstring,x)
            print(mainstring)
            
            

        else:
            return False
    return True        

print(check(s,p))



    






 

