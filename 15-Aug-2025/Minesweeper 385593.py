# Problem: Minesweeper - https://leetcode.com/problems/minesweeper/

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        x,y = click[0], click[1]
        n = len(board)
        m = len(board[0])

        if board[x][y] == "M":
            board[x][y] = "X"
            return board

        dirs = [(0,1),(0,-1),(1,0),(1,-1),(1,1),(-1,-1),(-1,0),(-1,1)]
        cnt = 0

        for i,j in dirs:
            if -1 < x+i < n and -1 < y+j < m:
                if board[x+i][y+j] == "M":
                    cnt += 1
        if cnt == 0:
            board[x][y] = "B"
            for i,j in dirs:
                if -1 < x+i < n and -1 < y+j < m:
                    if board[x+i][y+j] == "M" or board[x+i][y+j] == "E":
                        self.updateBoard(board,[x+i,y+j])
        else:
            board[x][y] = str(cnt)
        return board

        