# Problem: A - Escaping Prison - https://codeforces.com/gym/601269/problem/A

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
    n,h = numbers()
    c = 0
    for i in range(n):
        c += max(numbers())
    print(yn(c>=h))
    
    return
 
for _ in range(test(number())):
    solve()