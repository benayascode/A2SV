# Problem: A. Beautiful Matrix - https://codeforces.com/problemset/problem/263/A

matrix = []
flag = True
ind = [0,0]
 
 
for i in range(5):
    matrix.append(list(map(int,input().split())))
    if flag:
        for j in range(5):
            if matrix[i][j] == 1:
                flag = False
                ind = [i , j]
print(abs(ind[0] - 2) + abs(ind[1] - 2))