# Problem: C - Binary Flip - https://codeforces.com/gym/590053/problem/C

for _ in range(int(input())):
    n = int(input())
    a = input()
    b = input()
    
    count_0, count_1 = 0, 0
    for i in range(n):
        if a[i] == '0':
            count_0 += 1
        else:
            count_1 += 1
    # print(count_0)
    # print(count_1)
    
    flag2 = False  
    flag = True
    for i in range(n - 1, -1, -1): 
        if (not flag2 and a[i] != b[i]) or (flag2 and a[i] == b[i]):
            if count_0 != count_1:
                flag = False
                break
            flag2 = not flag2  
        
        if a[i] == '0':
            count_0 -= 1
        else:
            count_1 -= 1

    print("YES" if flag else "NO")
    
    