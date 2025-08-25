# Problem: Trapped in the Witch's Labyrinth - https://codeforces.com/problemset/problem/2034/C

import math, sys,heapq
from bisect import bisect_left, bisect_right
from collections import deque, defaultdict, Counter
from random import randint

ni = lambda: int(sys.stdin.readline().strip())
nsi = lambda: list(map(int, sys.stdin.readline().strip().split()))
wsi = lambda: sys.stdin.readline().strip().split()
wi = lambda: sys.stdin.readline().strip()
yn = lambda condition: 'YES' if condition else 'NO'
test = lambda inp=0: ni() if not inp else inp
randkey = randint(0, 100000)
xor = lambda x: x ^ randkey
sys.setrecursionlimit(10**6)

'''



'''

def rec(arr, flag, r, c, visited):

    dis = {"L": (0, -1), "R": (0, 1), "U": (-1, 0), "D": (1, 0)}

    if arr[r][c] == "?":
        return False
    if (r, c) in visited:
        return flag[r][c]

    visited.add((r, c))
    dr, dc = dis[arr[r][c]]
    nr, nc = r + dr, c + dc

    if nr < 0 or nc < 0 or nr >= len(arr) or nc >= len(arr[0]):
        flag[r][c] = True
        return True

    val = rec(arr, flag, nr, nc, visited)
    flag[r][c] = val
    return val


def solve():
    r, c = nsi()

    arr = [list(wi()) for _ in range(r)]
    flag = [[False] * c for _ in range(r)]
    out = 0

    visited = set()


    for i in range(r):
        for j in range(c):
            if (i, j) not in visited:
                val = rec(arr, flag, i, j, visited)
                flag[i][j] = val

    
    for i in range(r):
        for j in range(c):
            if arr[i][j] == "?":
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nr, nc = i + dr, j + dc
                    if 0 <= nr < r and 0 <= nc < c:
                        if flag[nr][nc] == False:
                            break
                else:
                    out -= 1
                out += 1
            else:
                if not flag[i][j]:
                    out += 1
    print(out)
    return

ttt = ni()
for _ in range(test(ttt)):
    solve()