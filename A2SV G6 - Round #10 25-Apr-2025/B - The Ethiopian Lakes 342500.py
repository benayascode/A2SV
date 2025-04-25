# Problem: B - The Ethiopian Lakes - https://codeforces.com/gym/602812/problem/B

# Betel
import math, sys
from bisect import bisect_left, bisect_right
from collections import deque, defaultdict, Counter
from random import randint

number = lambda: int(sys.stdin.readline().strip())
numbers = lambda: list(map(int, sys.stdin.readline().strip().split()))
words = lambda: sys.stdin.readline().strip().split()
word = lambda: sys.stdin.readline().strip()
yn = lambda condition: 'YES' if condition else 'NO'
test = lambda inp=0: number() if not inp else inp
jasjdfh = randint(0, 100000)
xor = lambda x: x ^ jasjdfh


 
 
def solve():
    n, m = numbers()
    mat = [numbers() for _ in range(n)]
    visited = []
    for _ in range(n):
        f = [0] * m
        visited.append(f)
    
    maxi = 0

    def dfs(i, j):
        st = [(i,j)]
        c = 0

        while st:
            x,y = st.pop()
            if visited[x][y]:
                continue
            visited[x][y] = 1
            c += mat[x][y]
            for xx,yy in [(-1,0),(0,-1),(0,1),(1,0)]:
                x1 = xx + x
                y1 = yy + y
                if 0 <= x1 < n and 0 <= y1 < m and not visited[x1][y1] and mat[x1][y1] > 0:
                    st.append((x1,y1))
        return c


    for i in range(n):
        for j in range(m):
            if not visited[i][j] and mat[i][j] > 0:
                maxi = max(maxi, dfs(i,j))

    print(maxi)
    
    return
 
for _ in range(test(number())):
    solve()