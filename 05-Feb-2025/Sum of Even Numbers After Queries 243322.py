# Problem: Sum of Even Numbers After Queries - https://leetcode.com/problems/sum-of-even-numbers-after-queries/description/

class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        tot = sum([i for i in nums if i % 2 == 0])
        out = []

        for a,b in queries:
            if nums[b] % 2:
                nums[b] += a
                if nums[b] % 2 == 0:
                    tot += nums[b]
                    out.append(tot)
                else:
                    out.append(tot)
            else:
                tot -= nums[b]
                nums[b] += a
                if nums[b] % 2 == 0:
                    tot += nums[b]
                    out.append(tot)
                else:
                    out.append(tot)
        return out
