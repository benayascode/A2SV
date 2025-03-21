# Problem: Christmas Spruce - https://codeforces.com/contest/913/problem/B

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
    child = []
    for i in range(n):
        child.append([])
    for i in range(n-1):
        x = number()
        child[x-1].append(i + 1)
    # print(child)
    for j in child:
        c = 0
        for i in j:
            if not len(child[i]):
                c += 1
        if j and c < 3:
            print("No")
            return
    print("Yes")

    
    return
 
for _ in range(test(1)):
    solve()