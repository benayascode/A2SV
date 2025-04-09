# Problem: C - Ras Alula and The Decrypted Messages - https://codeforces.com/gym/601269/problem/C

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
    n, m = numbers() 
    s = word() 
    strs = word()  
    
    stot = 0
    x = 0 
    for i in range(m):
        stot += (ord(strs[i])-96)
    for i in range(m):
        x += (ord(s[i]) - 96)
    
    f = 0
    for i in range(m, n):
        if x == stot:
            f = 1
            break
        
        x += (ord(s[i]) - 96)
        # print("xx1",x)
        x -= ord(s[i - m]) - 96
        # print("xxxxx2",x)
    

    if x == stot:
        # print(x,stot)
        f = 1
    
    print(yn(f))
 
for _ in range(test(number())):
    solve()