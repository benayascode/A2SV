# Problem: D - Bomb Detection Validation - https://codeforces.com/gym/586960/problem/D

n, m = map(int, input().split())
mat = []
for _ in range(n):
    mat.append(input().strip())


dir = [(-1, -1), (-1, 0), (-1, 1), (0, -1),(0, 1), (1, -1), (1, 0), (1, 1)]
    
for i in range(n):
    for j in range(m):
        if mat[i][j] == '*':
            continue
            
        c = 0
        for di, dj in dir:
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < m and mat[ni][nj] == '*':
                c += 1
            
        if mat[i][j] == '.':
            if c != 0:
                print("NO")
                exit()
        elif mat[i][j].isdigit():
            if c != int(mat[i][j]):
                print("NO")
                exit()
    
else:
    print("YES")