# Problem: Segments with Small Spread - https://codeforces.com/edu/course/2/lesson/9/2/practice/contest/307093/problem/F

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


 
 
def solve(n,a,k):
    mini = deque()
    maxi = deque()
    l = 0
    out = 0
    
    for r in range(n):
        while mini and a[mini[-1]] > a[r]:
            mini.pop()
        mini.append(r)
        
        while maxi and a[maxi[-1]] < a[r]:
            maxi.pop()
        maxi.append(r)
        
        while a[maxi[0]] - a[mini[0]] > k:
            l += 1
            if mini[0] < l:
                mini.popleft()
            if maxi[0] < l:
                maxi.popleft()
        
        out += (r - l + 1)
    
    return out

for _ in range(test(1)):
    n, k = numbers()
    a = numbers()
    print(solve(n, a, k))