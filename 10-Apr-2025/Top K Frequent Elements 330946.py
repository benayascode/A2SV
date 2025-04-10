# Problem: Top K Frequent Elements - https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mydict = Counter(nums)
        mydict = dict(sorted(mydict.items(),key = lambda x:x[1], reverse = True))
        out = list(mydict.keys())[:k]
        return out