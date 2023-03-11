#problem Link:  17. [Find Kth Bit in Nth Binary String](https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/)


#Take help from Youtube:

#Solution:


def findKthBit(self, N, K):
        ans = 1
        mid = (1 << (N - 1))
        while K > 1:
            if K == mid: return str(ans)
            if K > mid: 
                K = 2 * mid - K
                ans ^= 1
            mid >>= 1
        return str(ans^1)
