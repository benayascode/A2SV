# Problem: Insertion Sort - https://www.hackerrank.com/challenges/insertionsort1/problem


def insertionSort1(n, arr):
    # Write your code here
    temp = arr[-1]
    for j in range(n-2,-1,-1):
        if arr[j] > temp:
            arr[j+1] = arr[j]
            print(*arr) 
        else:
            arr[j+1] = temp
            break
    else:
        arr[0] = temp
    print(*arr)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)