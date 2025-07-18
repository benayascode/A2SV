# Problem: E - The Cooling Effect - https://codeforces.com/gym/591928/problem/E

import math, sys, heapq
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

def solve():
    x = input()
    n, k = nsi()
    pos = nsi()
    temp = nsi()
    total = [float('inf')] * n  
    for i in range(k):  
        total[pos[i] - 1] = temp[i]  

    fw = [float('inf')] * n  
    fw[0] = total[0]  
    for i in range(1, n):  
        fw[i] = min(fw[i - 1] + 1, total[i])  

    bw = [float('inf')] * n  
    bw[-1] = total[-1]  
    for i in range(n - 2, -1, -1):  
        bw[i] = min(bw[i + 1] + 1, total[i])  

    result = [min(fw[i], bw[i]) for i in range(n)]  
    print(*result)  

ttt = ni()
for _ in range(test(ttt)):
    solve()
