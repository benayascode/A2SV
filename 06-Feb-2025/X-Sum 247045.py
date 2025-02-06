# Problem: X-Sum - https://codeforces.com/problemset/problem/1676/D

for _ in range(int(input())):
    n , m = map(int,input().split())
    mat = []
    for __ in range(n):
        mat.append(list(map(int,input().split())))
    
    dig1 = {}
    dig2 = {}

    for i in range(n):
        for j in range(m):
            if i-j not in dig1:
                dig1[i-j] = 0
            dig1[i-j] += mat[i][j]

            if i+j not in dig2:
                dig2[i+j] = 0
            dig2[i+j] += mat[i][j]
    maxi = 0
    for i in range(n):
        for j in range(m):
            curr = dig1[i - j] + dig2[i + j] - mat[i][j]
            maxi = max(maxi, curr)
    print(maxi)
    
