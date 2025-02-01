# Problem: Odd Divisor - https://codeforces.com/problemset/problem/1475/A

for i in range(int(input())):
    x = int(input())
    if x%2 != 0:
        print("YES")
    else:

        if (x & (x-1)) == 0:
            print("NO")
        else:
            print("YES")