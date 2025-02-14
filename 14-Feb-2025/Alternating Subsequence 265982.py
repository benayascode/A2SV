# Problem: Alternating Subsequence - https://codeforces.com/contest/1343/problem/C

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    if n == 1:
        print(arr[0])
        continue

    l, r = 0, 1
    x = 0
    maxi = arr[l]
    for r in range(1,n):
        if arr[l] * arr[r] < 0:
            x += maxi
            maxi =  -1 * 10 ** 9 - 1
            l = r

        maxi = max(maxi,arr[r])
    print(x+maxi)