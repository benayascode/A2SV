# Problem: B - Empress Taytu and The Water Source - https://codeforces.com/gym/601269/problem/B

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
    n,k = numbers()
    d = numbers()
    a = numbers()

    def valid(m):
        c = 0
        for i, j in zip(d, a):
            x = math.ceil(i/m)
            c += x * j   
        return c <= k


    l , r = 1 , max(d)
    out = -1
    while l <= r:
        m = (l+r)//2
        if valid(m):
            out = m
            r = m-1
        else:
            l = m+1
    print(out)
    
    return
 
for _ in range(test(number())):
    solve()