# Problem: F - Nahom's Array Dilemma - https://codeforces.com/gym/594077/problem/F

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


 
 
def solve(n,a):
    pre = [0] * (n+1)
    st = []

    for i,j in enumerate(a):
        pre[i] = pre[i-1] + j
        while st and a[st[-1]] <= j:
            l = st.pop()
            if pre[i] - pre[l-1] > j:
                return 0

        st.append(i)
    return 1

    
    
    
    
    return
 
for _ in range(test(number())):
    n = number()
    a = numbers()
    ans =  solve(n,a) and solve(n,a[::-1])
    print(yn(ans))

 