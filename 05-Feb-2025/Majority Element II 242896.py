# Problem: Majority Element II - https://leetcode.com/problems/majority-element-ii/?envType=daily-question&envId=2023-10-05

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        k = len(nums)/3
        check = Counter(nums)
        out = []
        for key,value in check.items():
            if value > k:
                out.append(key)
        return out