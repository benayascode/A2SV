# Problem: Odd Subarrays - https://codeforces.com/problemset/problem/1686/B

import math, sys

number = lambda: int(sys.stdin.readline().strip())
numbers = lambda: list(map(int, sys.stdin.readline().strip().split()))
test = lambda inp=0: number() if not inp else inp

 
 
def solve():
    n = number()
    arr = numbers()
    if n == 1:
        print(0)
        return
    l,r = 0 ,1
    c = 0
    while r < n:
        if arr[l] > arr[r]:
            c += 1
            l += 1
            r += 1
        
        l += 1
        r += 1
    
    print(c)
 
    
    return
 
for _ in range(test(number())):
    solve()