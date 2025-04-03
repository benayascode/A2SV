# Problem: Sereja and Dima - https://codeforces.com/problemset/problem/381/A

# Betel
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
    n = number()
    a = numbers()
    s , d = 0, 0
    l , r = 0 , n-1
    f = 1
    while r >= l:
        if a[l] > a[r]:
            x = a[l]
            l += 1
        else:
            x = a[r]
            r -= 1
        if f:
            s += x
            f = 0
        else:
            d += x
            f = 1
    print(s,d)


    
    return
 
for _ in range(test(1)):
    solve()