# Problem: Count Good Numbers - https://leetcode.com/problems/count-good-numbers/

class Solution:
    def countGoodNumbers(self, n: int) -> int:
        even = (n + 1) // 2
        odd = n // 2
        return (pow(5, even, 10**9 + 7) * pow(4, odd, 10**9 + 7)) % (10**9 + 7)