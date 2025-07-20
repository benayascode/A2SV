# Problem:  Network Topology - https://codeforces.com/problemset/problem/292/B

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
    n,m = numbers()
    a =[[] for i in range(n+1)]
    for _ in range(m):
        x,y = numbers()
        a[x].append(y)
        a[y].append(x)
    o,t,s = 0,0,0

    for i in range(1,n+1):
        c = len(a[i])
        if c == 1:
            o += 1
        elif c == 2:
            t += 1
        elif c == n-1:
            s += 1

    if o == n-1 and s == 1:
        print("star topology")
    elif o == 2 and t == n-2:
        print("bus topology")
    elif t == n:
        print("ring topology")
    else:
        print("unknown topology")


    
    return
 
for _ in range(test(1)):
    solve()