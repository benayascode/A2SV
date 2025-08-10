# Problem: Find K Closest Elements - https://leetcode.com/problems/find-k-closest-elements/

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if len(arr) == k:
            return arr
        n = len(arr)

        pvt = bisect_left(arr,x)
        l,r,q = pvt-1,pvt,deque()

        while len(q) < k:
            if r < n and abs(arr[r]-x) < abs(arr[l]-x):
                q.append(arr[r])
                r += 1
            else:
                q.appendleft(arr[l])
                l -= 1
        return list(q)
