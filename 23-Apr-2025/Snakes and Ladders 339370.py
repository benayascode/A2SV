# Problem: Snakes and Ladders - https://leetcode.com/problems/snakes-and-ladders/

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        cord = {}
        nums = 1

        for i in range(n - 1, -1, -1):
            row = range(n) if (n-i) % 2  else range(n - 1, -1, -1)
            for j in row:
                cord[nums] = (i, j)
                nums += 1

        q = deque([(1, 0)]) 
        visited = set()

        while q:
            s, m = q.popleft()
            for i in range(1, 7):
                nxt = s + i
                if nxt > n * n:
                    continue
                r, c = cord[nxt]
                if board[r][c] != -1:
                    nxt = board[r][c]
                if nxt == n * n:
                    return m + 1
                if nxt not in visited:
                    visited.add(nxt)
                    q.append((nxt, m + 1))

        return -1




        

        