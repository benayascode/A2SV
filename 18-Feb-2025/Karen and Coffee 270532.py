# Problem: Karen and Coffee - https://codeforces.com/contest/816/problem/B

n , k , q = map(int,input().split())
coffee = []
for _ in range(n):
    a,b = map(int,input().split())
    coffee.append([a,b])

qry = []
for _ in range(q):
    a,b = map(int,input().split())
    qry.append([a,b])

x = min(coffee)
y = max(i for j,i in coffee)
z = max(i for j,i in qry)
y = max(y,z)
cof = [0] * (y+10)


for a,b in coffee:
    cof[a] += 1
    cof[b+1] -= 1

for i in range(1,z+1):
    cof[i] += cof[i-1]

for i in range(len(cof)):
    if cof[i] >= k:
        cof[i] = 1
    else:
        cof[i] = 0



for i in range(1,z+1):
    cof[i] += cof[i-1]

for a,b in qry:
    out = 0
    out += cof[b] - cof[a-1]
    print(out)