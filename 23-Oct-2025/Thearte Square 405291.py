# Problem: Thearte Square - https://codeforces.com/problemset/problem/1/A

import math, sys
from bisect import bisect_left, bisect_right
from collections import deque, defaultdict, Counter
from random import randint

number = lambda: int(sys.stdin.readline().strip())
numbers = lambda: list(map(int, sys.stdin.readline().strip().split()))
words = lambda: sys.stdin.readline().strip().split()
word = lambda: sys.stdin.readline().strip()
yn = lambda condition: 'YES' if condition else 'NO'
test = lambda inp=0: number() if not inp else inp
jasjdfh = randint(0, 100000)
xor = lambda x: x ^ jasjdfh

def solve():
    n, m, a = numbers()
    print((math.ceil(n / a)) * (math.ceil(m / a)))

for _ in range(test(1)):
    solve()