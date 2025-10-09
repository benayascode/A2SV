# Problem: Check If Array Pairs Are Divisible by k - https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        mydict = Counter([i%k for i in arr])
        for i in range(k):
            if i == 0:
                if mydict[i]%2:
                    return False
            else:
                if mydict[i] != mydict[k-i]:
                    return False
        return True