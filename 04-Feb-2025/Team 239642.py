# Problem: Team - https://codeforces.com/contest/231/problem/A

p = 0

for i in range(int(input())):
    a,b,c = map(int,input().split())
    if a + b + c > 1:
        p += 1
print(p)