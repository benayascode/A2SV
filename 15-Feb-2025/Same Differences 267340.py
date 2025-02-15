# Problem: Same Differences - https://codeforces.com/problemset/problem/1520/D

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    a = {}
    res = 0
    for i in range(n):
        x = arr[i]
        x -= i
        if x in a:
            res += a[x]
        else:
            a[x] = 0
        a[x] += 1
    print(res)