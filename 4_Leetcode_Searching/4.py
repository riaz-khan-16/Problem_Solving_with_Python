#[Two Sum II - Input array is sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)


numbers = [2,3,4]
target = 6


def find(numbers,target):
    start=0
    end=len(numbers)-1
    while start<end:
        if numbers[start]+numbers[end]==target:
            return start+1, end+1
        elif numbers[start]+numbers[end]>target:
            end=end-1
        else:
            start=start+1
print(find(numbers,target))                   


   


    