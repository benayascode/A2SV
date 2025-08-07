# Problem: Minimum Number of Pushes to Type Word II - https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-ii/

class Solution:
    def minimumPushes(self, word: str) -> int:
        cnt = Counter(word)
        arr = list(sorted(cnt.values()))[::-1]
        if len(arr) < 9:
            return len(word)

        out = 0
        i = 0
        k = 1
        n = len(arr)
        if n < 17:
            x = sum(arr[:8])
            y = sum(arr[8:])
            return x + (2*y)
        elif n < 25:
            x = sum(arr[:8])
            y = sum(arr[8:16])
            z = sum(arr[16:])
            return x + (2*y) + (3*z)
        else:
            x = sum(arr[:8])
            y = sum(arr[8:16])
            z = sum(arr[16:24])
            w = sum(arr[24:])
            return x + (2*y) + (3*z) + (4*w)
        