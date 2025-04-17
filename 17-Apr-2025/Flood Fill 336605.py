# Problem: Flood Fill - https://leetcode.com/problems/flood-fill/

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image
        cur_col = image[sr][sc]
        
        def dfs(i,j):
            if not 0 <= i < len(image) or not 0 <= j < len(image[0]):
                return

            if cur_col != image[i][j]:return

            image[i][j] = color

            for x,y in ([0,1],[0,-1],[1,0],[-1,0]):
                dfs(i+x,j+y)
        dfs(sr,sc)
        return image


