#66. Plus One
# https://leetcode.com/problems/plus-one/

digits = [1,2,3]

#array to integer
def arrayToInteger(digits):
        a=digits
        b=''
        for i in a:
            b=b+str(i)
        return b
integer=arrayToInteger(digits)     

#add 1
integer=int(arrayToInteger(digits)) +1
#integer ro array

def IntegerToArray(integer):
            array=[]
            for i in str(integer):
                array.append(int(i))
            return array
print(IntegerToArray(integer))            