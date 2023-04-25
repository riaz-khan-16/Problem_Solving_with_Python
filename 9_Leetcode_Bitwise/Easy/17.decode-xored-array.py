# 17. [Decode XORed Array](https://leetcode.com/problems/decode-xored-array/)




encoded = [1,2,3]
first = 1
arr = [first]
for i in range(0, len(encoded)):
    arr.append(arr[i] ^ encoded[i])
print(arr)