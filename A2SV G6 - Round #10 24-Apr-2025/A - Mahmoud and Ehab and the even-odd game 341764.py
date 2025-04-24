# Problem: A - Mahmoud and Ehab and the even-odd game - https://codeforces.com/gym/602812/problem/A

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
    if n % 2:
        print("Ehab")
    else:
        print("Mahmoud")
    return
 
for _ in range(test(1)):
    solve()