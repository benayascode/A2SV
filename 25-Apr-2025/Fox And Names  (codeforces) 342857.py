# Problem: Fox And Names  (codeforces) - https://codeforces.com/contest/510/problem/C

import math, sys
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

'''



'''
def solve():
    n = ni()
    s = [wi() for _ in range(n)]
    
    indeg = defaultdict(int)
    graph = defaultdict(list)
    queue = deque()
    out = []


    for i in range(26):
        graph[chr(97+i)]
    # print(graph)

    for i in range(1,n):
        frst , scnd = s[i-1] , s[i]
        flag = 0

        for j in range(min(len(frst),len(scnd))):
            if frst[j] != scnd[j]:
                graph[frst[j]].append(scnd[j])
                indeg[scnd[j]] += 1
                flag = 1
                break
         
        if not flag and len(frst) > len(scnd):
            print("Impossible")
            return
    
    # print(graph)
    # print(indeg)
    for i in graph:
        if indeg[i] == 0:
            queue.append(i)

    while queue:
        q = queue.popleft()
        out.append(q)

        for i in graph[q]:
            indeg[i] -= 1

            if indeg[i] == 0:
                queue.append(i)
    
    if len(out) != 26:print("Impossible")
    else:print("".join(out))






    return

ttt = 1
for _ in range(test(ttt)):
    solve()


