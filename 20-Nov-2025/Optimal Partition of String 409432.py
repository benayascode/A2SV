# Problem: Optimal Partition of String - https://leetcode.com/problems/optimal-partition-of-string/

class Solution:
    def partitionString(self, s: str) -> int:
        set_ = set()

        c = 1
        for i in s:
            if i in set_:
                c += 1
                set_ = set()
            set_.add(i)
        return c