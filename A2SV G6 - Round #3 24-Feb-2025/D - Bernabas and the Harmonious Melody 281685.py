# Problem: D - Bernabas and the Harmonious Melody - https://codeforces.com/gym/588468/problem/D

def palin(s):
    return s == s[::-1]

def dell(s):
    n = len(s)
    dell = float('inf')
    
    for char in set(s):
        l, r = 0, n - 1
        x = 0
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            elif s[l] == char:
                l += 1
                x += 1
            elif s[r] == char:
                r -= 1
                x += 1
            else:
                x = float('inf')
                break
        
        dell = min(dell, x)

    return dell if dell != float('inf') else -1

t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    if palin(s):
        print(0)
    else:
        print(dell(s))





     
                