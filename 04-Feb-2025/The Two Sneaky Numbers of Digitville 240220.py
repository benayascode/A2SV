# Problem: The Two Sneaky Numbers of Digitville - https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/description

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        out = []
        for i in range(len(nums)-2):
            if c[i] > 1:
                out.append(i)
                if len(out) > 1:
                    return out
                    
        