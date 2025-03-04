# Problem: Array Splitting - https://codeforces.com/problemset/problem/1175/D


import math, sys

number = lambda: int(sys.stdin.readline().strip())
numbers = lambda: list(map(int, sys.stdin.readline().strip().split()))
test = lambda inp=0: number() if not inp else inp


 
 
def solve():
    n,k = numbers()
    arr = numbers()
    
    

    for i in range(n-2,-1,-1):
        arr[i] += arr[i+1]

    x= arr[0]
    arr.pop(0)
    out = 0
    arr.sort()
    # print(arr)
    out += sum(arr[n-k:])
    print(out+x)
    


    
    return
 
for _ in range(test(1)):
    solve()