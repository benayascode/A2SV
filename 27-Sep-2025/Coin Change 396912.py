# Problem: Coin Change - https://leetcode.com/problems/coin-change/

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dp(n):
            if n < 0:
                return -1
            if n == 0:
                return 0
            if n in memo:
                return memo[n]

            mini = float('inf')
            for i in coins:
                out = dp(n-i)
                if out != -1:
                    mini = min(mini,1+out)

            memo[n] = mini if mini != float('inf') else -1
            return memo[n]

        return dp(amount)