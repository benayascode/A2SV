# Problem: Find Champion II - https://leetcode.com/problems/find-champion-ii/

class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        indeg = [0] * n

        for a,b in edges:
            indeg[b] += 1

        arr = [i for i in range(n) if indeg[i] == 0]
        if len(arr) == 1:
            return arr[0]
        return -1