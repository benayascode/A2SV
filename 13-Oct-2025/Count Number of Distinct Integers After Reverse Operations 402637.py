# Problem: Count Number of Distinct Integers After Reverse Operations - https://leetcode.com/problems/count-number-of-distinct-integers-after-reverse-operations/

class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        set_ = set(nums)
        c = len(set_)

        for i in nums:
            x = int(str(i)[::-1])
            if x not in set_:
                c += 1
                set_.add(x)
        return c