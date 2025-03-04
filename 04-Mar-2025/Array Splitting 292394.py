# Problem: Array Splitting - https://codeforces.com/problemset/problem/1197/C

# Betel
import math, sys

number = lambda: int(sys.stdin.readline().strip())
numbers = lambda: list(map(int, sys.stdin.readline().strip().split()))
test = lambda inp=0: number() if not inp else inp


 
 
def solve():
    n,k= numbers()
    arr = numbers()

    predif = [0] * (n-1)
    for i in range(1,n):
        predif[i-1] = arr[i] - arr[i-1]
    predif.sort()
    # print(predif)
 
    
    print(sum(predif[:n-k]))
    
    return
 
for _ in range(test(1)):
    solve()