# Problem: Tuple with Same Product - http://leetcode.com/problems/tuple-with-same-product

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        out = 0
        c = collections.Counter()
        for i in range(len(nums)):
            for j in range(i):
                p = nums[i] * nums[j]
                c[p] += 1

        for k,v in c.items():
            out += (v*(v-1))//2

        return out * 8