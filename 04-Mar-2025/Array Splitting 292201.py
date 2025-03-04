# Problem: Array Splitting - https://codeforces.com/problemset/problem/1197/C

# Betel
import math, sys

number = lambda: int(sys.stdin.readline().strip())
numbers = lambda: list(map(int, sys.stdin.readline().strip().split()))
test = lambda inp=0: number() if not inp else inp



def solve():
    n,k= numbers()
    a = numbers()

    predif = [0]*n
    for i in range(1, n):
        predif[i] = a[i - 1] - a[i] 

    predif.sort()
    out = a[-1] - a[0]
    for i in range(k - 1):
        out += predif[i]
    
    print(out)
    
    
    
    return
 
for _ in range(test(1)):
    solve()