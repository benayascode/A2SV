# Problem: Nested Lists - https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true

if __name__ == '__main__':
    mydict = {}
    for _ in range(int(input())):
        name = input()
        score = float(input())
        if score in mydict:
            mydict[score].append(name)
        else:
            mydict[score] = [name]
    orders = sorted(mydict.keys())

    sec = orders[1]
    names = sorted(mydict[sec])
    for name in names:
        print(name) 