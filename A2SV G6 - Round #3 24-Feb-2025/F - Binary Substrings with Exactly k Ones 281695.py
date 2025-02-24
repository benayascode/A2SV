# Problem: F - Binary Substrings with Exactly k Ones - https://codeforces.com/gym/588468/problem/F

k = int(input())
s = input()
n = len(s)

if k == 0:
    cnt0 = 0
    zero = 0
    for i in s:
        if i == '0':
            zero += 1
            cnt0 += zero
        else:
            zero = 0
    print(cnt0)
else:
    out = {}
    out[0] = 1 
    ind = 0
    result = 0

    for i in s:
        if i == '1':
            ind += 1

        if (ind - k) in out:
            result += out[ind - k]

        if ind in out:
            out[ind] += 1
        else:
            out[ind] = 1

    print(result)