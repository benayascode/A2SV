# Problem: B - Anansi and Trip-Photographs - https://codeforces.com/gym/588468/problem/B

for _ in range(int(input())):
    n , x = map(int,input().split())
    h = list(map(int,input().split()))
    if n == 1:
        if abs(h[1] - h[0]) >= x:
            print("YES")
        else:
            print("NO")
        continue
    h.sort()
    l , r = n-1, n*2 -1
    while l > -1:
        if h[r] - h[l] < x:
            print("NO")
            break
        r -= 1
        l -= 1
    else:
        print("YES")