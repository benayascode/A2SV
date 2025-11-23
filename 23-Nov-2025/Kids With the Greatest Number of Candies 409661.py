# Problem: Kids With the Greatest Number of Candies - https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxi = max(candies)
        out = [True] * (len(candies))
        for i in range(len(candies)):
            if candies[i] + extraCandies < maxi:
                out[i] = False
        return out