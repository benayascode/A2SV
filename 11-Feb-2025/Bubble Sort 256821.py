# Problem: Bubble Sort - https://www.hackerrank.com/challenges/ctci-bubble-sort/problem

def countSwaps(a):
    # Write your code here
    swap = 0
    n = len(a)
    for i in range(n):
        c = 1
        for j in range(1,n-i):
            if a[j] < a[j-1]:
                c = 0
                swap += 1
                a[j-1], a[j] = a[j],a[j-1]
        if c:
            break
    print("Array is sorted in "+str(swap)+" swaps.")
    print("First Element: "+str((a[0])))
    print("Last Element: "+str(a[-1]))


        

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)