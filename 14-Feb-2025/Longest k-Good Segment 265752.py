# Problem: Longest k-Good Segment - https://codeforces.com/problemset/problem/616/D

n , k = map(int,input().split())
arr = list(map(int,input().split()))

mydict = {}
l = 0 
out = [0 ,0]
m = k

for r in range(n):
    if arr[r] not in mydict:
        if len(mydict) == k:
            temp = arr[l]
            while len(mydict) >= k:
                mydict[arr[l]] -= 1
                if mydict[arr[l]] == 0:
                    del mydict[arr[l]]
                l += 1
        mydict[arr[r]] = 1

    else:
        mydict[arr[r]] += 1

    if (r-l+1) > (out[1]-out[0]):
        out = [l+1,r+1]
print(*out)
    

