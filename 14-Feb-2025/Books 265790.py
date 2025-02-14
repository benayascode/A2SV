# Problem: Books - https://codeforces.com/contest/279/problem/B

n , t = map(int,input().split())
arr = list(map(int,input().split()))

maxi = 0
l ,r = 0 , 0
tot = 0

while r < n:
    tot += arr[r]
    if tot > t:
        while tot > t:
            tot -= arr[l]
            l += 1

    maxi = max(maxi,r-l+1)
    r += 1
print(maxi)
    