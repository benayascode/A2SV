# Problem: Minimum Number of Days to Make m Bouquets - https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        
        if m * k > len(bloomDay):
            return -1
        
        def helper(mid):
            flr = bqts = 0
            for i in bloomDay:
                if i <= mid:
                    flr += 1
                    if flr == k:
                        bqts += 1
                        flr = 0
                        if bqts >= m:
                            return True
                else:
                    flr = 0
            return False
        
        l, r = min(bloomDay), max(bloomDay)
        while l <= r:
            mid = (l + r) // 2
            if helper(mid):
                r = mid - 1
            else:
                l = mid + 1
        return l