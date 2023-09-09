# 1. [Next greater element I](https://leetcode.com/problems/next-greater-element-i/) leetcode


nums1 = [4,1,2]
nums2 = [1,3,4,2]

nums1 = [2,4]
nums2 = [1,2,3,4]



#brute force

# Take an element from nums1 
# find the element in nums 2
# find its index
# traverse the next indices and check weather any greater elelment available or not
# if  available take that and insert in output
# if not available insert -1  in output
# back to the nums1 and take another element


def brute_force(nums1,nums2):
    output=[]
# Take an element from nums1 
    i=0
    while i<len(nums1):
        e=nums1[i]
        for k in range(len(nums2)):
            if e==nums2[k]: # find the element in nums 2
                       # find its index
                n=-1
                for l in range(k+1,len(nums2)):
                    if nums2[l]>e:
                        n=nums2[l]
                        break
                output.append(n)        
        i=i+1
    return output



#Using Hash Map
nums1 = [4,1,2]
nums2 = [1,3,4,2]

nums1 = [2,4]
nums2 = [1,2,3,4]

#find the next greater of every elements and make an array
def using_hash(nums1,nums2):
    hash={}
    new=[]

    for i in range(len(nums2)):
        element=nums2[i]
        print("elememnt: "+ str(element))
        next_greater=-1
        for j in range(i+1,len(nums2)):
            
            if nums2[j]>element:
                next_greater=nums2[j]
                break
        print("next_greater: "+ str(next_greater))    
        new.append(next_greater)
    print(new)    
    #make a hashmapp  

    for i in range(len(nums2)):
        hash[nums2[i]]=new[i]    
    #Traverse the hashmap
    output=[]
    for i in nums1:
        output.append(hash[i])

    return output


print(using_hash(nums1,nums2))
    






