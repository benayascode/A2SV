# Problem: Red and Blue - https://codeforces.com/contest/1469/problem/B

# Betel
import math, sys

number = lambda: int(sys.stdin.readline().strip())
numbers = lambda: list(map(int, sys.stdin.readline().strip().split()))
test = lambda inp=0: number() if not inp else inp


 
 
def solve():
    n = number()
    a = numbers()
    m = number()
    b = numbers()

    pre1 = [a[0]]*n
    pre2 = [b[0]]*m

    for i in range(1,n):
        pre1[i] = pre1[i-1] + a[i]
    for i in range(1,m):
        pre2[i] = pre2[i-1] + b[i]

    x = max(pre1)
    y = max(pre2)
    print(max(0,x,y,x+y)) 
    
    return
 
for _ in range(test(number())):
    solve()