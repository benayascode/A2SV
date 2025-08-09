# Problem: Permutation Sequence - https://leetcode.com/problems/permutation-sequence/description/

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = list(range(1,n+1))
        f = factorial(n) // n
        k -= 1
        out = []

        while nums:
            out.append(str(nums[k//f]))
            nums.pop(k//f)
            k %= f
            if not nums:
                break
            f //= (len(nums))
        return "".join(out)