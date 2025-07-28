# Problem: Construct Quad Tree - https://leetcode.com/problems/construct-quad-tree/description/

"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def dfs(n,r,c):
            allsame = 1
            for i in range(n):
                for j in range(n):
                    if grid[r][c] != grid[r+i][c+j]:
                        allsame = 0
                        break
            if allsame:
                return Node(grid[r][c],True)
            
            n //= 2
            tl = dfs(n,r,c)
            tr = dfs(n,r,c+n)
            bl = dfs(n,r+n,c)
            br = dfs(n,r+n,c+n)

            return Node(0,False, tl, tr, bl, br)

        return dfs(len(grid),0,0)
            

