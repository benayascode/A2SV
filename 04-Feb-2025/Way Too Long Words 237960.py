# Problem: Way Too Long Words - https://codeforces.com/problemset/problem/71/A

t = int(input())
for i in range(t):
    s = input()
    if len(s) < 11:
        print(s)
    else:
        print(s[0]+str(len(s)-2)+s[-1])