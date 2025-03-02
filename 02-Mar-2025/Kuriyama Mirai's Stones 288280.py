# Problem: Kuriyama Mirai's Stones - https://codeforces.com/contest/433/problem/B

n = int(input())
a = list(map(int,input().split()))
b = sorted(a)
for i in range(1,n):
    a[i] += a[i-1]
    b[i] += b[i-1]
a = [0]+a
b =[0] + b

m = int(input())
for i in range(m):
    t,l,r = map(int,input().split())
    if t == 1:
        print(a[r]-a[l-1])
    else:
        print(b[r]-b[l-1])