# Problem: Hamming Distance - https://leetcode.com/problems/hamming-distance/

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        n = x ^ y
        # print(bin(n))
        return (bin(n).count("1"))
        