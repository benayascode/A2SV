# Problem: H - Dominoes - https://codeforces.com/gym/589822/problem/H

r, c = list(map(int, input().split()))

grid = [[x for x in input()] for _ in range(r)]

side = [[0] * (c + 1) for _ in range(r + 1)]

up = [[0] * (c + 1) for _ in range(r + 1)]


dir = [(-1, 0), (0, -1)]

for nr in range(r):
    for nc in range(c):
        if grid[nr][nc] != ".":
            continue
        for x, y in dir:
            if nr - 1 >= 0 and nr - 1 < r and grid[nr - 1][nc] == ".":
                up[nr + 1][nc + 1] = 1
            if nc - 1 >= 0 and nc - 1 < c and grid[nr][nc - 1] == ".":
                side[nr + 1][nc + 1] = 1

for i in range(1, r + 1):
    for j in range(1, c + 1):
        up[i][j] += up[i - 1][j] + up[i][j - 1] - up[i - 1][j - 1]

for i in range(1, r + 1):
    for j in range(1, c + 1):
        side[i][j] += side[i - 1][j] + side[i][j - 1] - side[i - 1][j - 1]

q = int(input())


for _ in range(q):
    row1, col1, row2, col2 = list(map(int, input().split()))
    ups = (
        up[row2][col2]
        - up[row1][col2]
        - up[row2][col1 - 1]
        + up[row1][col1 - 1]
    )
    sides = (
        side[row2][col2]
        - side[row1 - 1][col2]
        - side[row2][col1]
        + side[row1 - 1][col1]
    )
    print(ups + sides)