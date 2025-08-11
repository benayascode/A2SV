# Problem: N Queens - https://leetcode.com/problems/n-queens/

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        diag1 = set()  
        diag2 = set()  
        out = []
        board = [["."] * n for _ in range(n)]

        def bt(r):
            if r == n:
                copy = ["".join(row) for row in board]
                out.append(copy)
                return

            for c in range(n):
                if c in col or (r + c) in diag1 or (r - c) in diag2:
                    continue

                col.add(c)
                diag1.add(r + c)
                diag2.add(r - c)
                board[r][c] = "Q"

                bt(r + 1)

                col.remove(c)
                diag1.remove(r + c)
                diag2.remove(r - c)
                board[r][c] = "."

        bt(0)
        return out
