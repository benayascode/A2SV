# Problem: B - Special Matrix Quest - https://codeforces.com/gym/586960/problem/B

n = int(input())
mat = []
for _ in range(n):
    mat.append(list(map(int, input().split())))


m = n // 2
out = 0

for i in range(n):
    out += mat[i][i]

for i in range(n):
    out += mat[i][n-i-1]

for i in range(n):
    out += mat[m][i]

for i in range(n):
    out += mat[i][m]
out -= (3 * mat[m][m])
print(out)