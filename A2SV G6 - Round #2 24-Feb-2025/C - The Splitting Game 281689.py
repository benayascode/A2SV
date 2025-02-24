# Problem: C - The Splitting Game - https://codeforces.com/gym/586960/problem/C

for _ in range(int(input())):
    n = int(input())
    s = input()
    ldict = {}
    rdict = {}

    for i in s:
        if i in rdict:
            rdict[i] += 1
        else:
            rdict[i] = 1

    out = 0
    l = 0
    r = len(rdict)

    for i in range(n - 1):
        if s[i] in ldict:
            ldict[s[i]] += 1
        else:
            ldict[s[i]] = 1
            l += 1

        rdict[s[i]] -= 1
        if rdict[s[i]] == 0:
            r -= 1

        out = max(out, l + r)

    print(out)