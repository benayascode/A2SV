# Problem: Lists - https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true

if __name__ == '__main__':
    N = int(input())
    out = []
    for i in range(N):
        command = input().split()
        if command[0] == "insert":
            out.insert(int(command[1]), int(command[2]))
        elif command[0] == "append":
            out.append(int(command[1]))
        elif command[0] == "remove":
            out.remove(int(command[1]))
        elif command[0] == "sort":
            out.sort()
        elif command[0] == "print":
            print(out)
        elif command[0] == "pop":
            out.pop()
        else:
            out.reverse()
            