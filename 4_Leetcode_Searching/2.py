#[Guess Number Higher or Lower](https://leetcode.com/problems/guess-number-higher-or-lower/)


n=10
start=1
end=n
def find(n):
    while True:
        mid=(start+end)//2
        res=guess(mid) #build in function
        if res==-1:
            end=mid-1
        if res==1:
            start=mid+1
        if res==0:
            return mid  
        

