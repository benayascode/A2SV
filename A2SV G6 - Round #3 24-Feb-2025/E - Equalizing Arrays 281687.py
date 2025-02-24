# Problem: E - Equalizing Arrays - https://codeforces.com/gym/588468/problem/E

a = int(input())
arr1 = list(map(int,input().split()))
b = int(input())
arr2 = list(map(int,input().split()))

if sum(arr1) != sum(arr2) :
    print(-1)
    exit()

if arr1 == arr2:
    print(a)

else:
    for i in range(1,a):
        arr1[i] += arr1[i-1]
    for i in range(1,b):
        arr2[i] += arr2[i-1]


    p1,p2 = 0 , 0
    c = 0

    while p1 < a and p2 < b:
        if arr1[p1] == arr2[p2]:
            p1 += 1
            p2 += 1
            c += 1
        elif arr1[p1] > arr2[p2]:
            p2 += 1
        else:
            p1 += 1
    if p1 == a and p2 == b:
        print(c)
    else:
        print(-1)