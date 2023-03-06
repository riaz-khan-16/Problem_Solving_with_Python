#problem Link:   3. [Number of Ways to Split a String](https://leetcode.com/problems/number-of-ways-to-split-a-string/)

#Take help from Youtube: https://www.youtube.com/watch?v=TSX__xdfOM8

#Solution:


def numWays(s):

        a=s
        n=len(a)
        print(n)

        if a.count('1')==0:
                return ((n-1)*(n-2)//2)

        if a.count('1')%3!=0:
                return (0)

        def findMN(a):
            r=a.count('1')/3
            o=0
            i=0
            while o<r:
                    if a[i]=='1':
                            o=o+1      
                    i=i+1
            j=len(a)-1
            p=0
            while p<r:
                    if a[j]=='1':
                            p=p+1     
                    j=j-1
            return i-1,j+1


    
        x,y=findMN(a)
        m=a[x+1:y]
        i=0
        while m[i]=='0':
            i=i+1   
        j=len(m)-1
        k=0
        while m[j]=='0':
            j=j-1
            k=k+1

        return ((i+1)*(k+1))

#         #Passed 160 cases



# # Collected method 

# #failed in 
print(numWays(x))

def numWays(self, s: str) -> int:
        ones = 0

        # Count number of Ones
        for char in s:
            if char == "1":
                ones += 1

        # Can't be grouped equally if the ones are not divisible by 3
        if ones > 0 and ones % 3 != 0:
            return 0

        # Ways of selecting two dividers from n - 1 dividers 
        if ones == 0:
            n = len(s)
			# n = {3: 1, 4: 3, 5: 6, 6: 10, 7: 15 ... }
            return (((n - 1) * (n - 2)) // 2) % ((10 ** 9) + 7)

        # Number of ones in each group
        ones_interval = ones // 3

        # Number of zeroes which lie on the borders
        left, right = 0, 0

        # Iterator
        i = 0
        temp = 0

        # Finding the zeroes on the left and right border
        while i < len(s):
            temp += int(s[i]) & 1
            if temp == ones_interval:
                if s[i] == '0':
                    left += 1
            if temp == 2 * ones_interval:
                if s[i] == '0':
                    right += 1
            i += 1
        
#         # The result is the product of number of (left + 1) and (right + 1)
#         # Because let's assume it as we only want to fill up the middle group
#         # The solution would be if we have zero then there might be a zero in the middle
#         # Or there might not be the zero, so this might case is added and then
# 		# the events are independent so product of both the events
        return ((left + 1) * (right + 1)) % ((10 ** 9) + 7)



   