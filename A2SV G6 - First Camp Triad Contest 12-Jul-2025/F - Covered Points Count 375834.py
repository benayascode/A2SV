# Problem: F - Covered Points Count - https://codeforces.com/gym/589822/problem/F

from collections import defaultdict

n = int(input())

mydict = defaultdict(int)

res = [0] * n

for _ in range(n):
    left, right = list(map(int, input().split()))
    mydict[left] += 1
    mydict[right + 1] -= 1

pair = sorted(mydict.items())

out = 0

for i in range(len(pair) - 1):
    num, freq = pair[i]
    x, _ = pair[i + 1]
    out += freq
    if out != 0:
        res[out - 1] += (
            x - num
        )  
print(*res)