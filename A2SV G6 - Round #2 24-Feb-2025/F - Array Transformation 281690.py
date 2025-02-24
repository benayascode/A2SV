# Problem: F - Array Transformation - https://codeforces.com/gym/586960/problem/F

from collections import Counter

for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))
    mydict = Counter(nums)
    val = list(mydict.values())
    
    val.sort()
    prefix = [0] * (len(val) + 1)
    for i in range(1, len(val) + 1):
        prefix[i] = prefix[i - 1] + val[i - 1]

    total = float('inf')  
    
    for i, v in enumerate(val):
        w = len(val) - (i + 1)
        h = v
        area = w*h
        ctot = (prefix[-1]-prefix[i + 1]) -area 
        total = min(total, prefix[i] + ctot)

    print(total)