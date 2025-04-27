# Problem: E - Machine Testing - https://codeforces.com/gym/601269/problem/E

import math, sys
from bisect import bisect_left, bisect_right
from collections import deque, defaultdict, Counter
from random import randint

ni = lambda: int(sys.stdin.readline().strip())
nsi = lambda: list(map(int, sys.stdin.readline().strip().split()))
wsi = lambda: sys.stdin.readline().strip().split()
wi = lambda: sys.stdin.readline().strip()
yn = lambda condition: 'YES' if condition else 'NO'
test = lambda inp=0: ni() if not inp else inp
randkey = randint(0, 100000)
xor = lambda x: x ^ randkey

'''

'''

def solve():
    n = ni()
    health = nsi()
    power = nsi()
    
    stack = [(math.inf, power[0])]
    ans = 0
    for i in range(1, n):
        time = 0
        while health[i] - (stack[-1][0] - time) * stack[-1][-1] > 0:
            t, p = stack.pop()
            health[i] -= (t - time) * p
            time += (t - time)
        time += math.ceil(health[i] / stack[-1][-1])
        stack.append((time, power[i]))
        ans = max(ans, time)
    
    print(ans)
    return

ttt = ni()
for _ in range(test(ttt)):
    solve()
