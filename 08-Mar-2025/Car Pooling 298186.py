# Problem: Car Pooling - https://leetcode.com/problems/car-pooling/description/

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        arr = [0] * 1000
        for n,l,r in trips:
            for i in range(l,r):
                arr[i] += n
                if arr[i] > capacity:
                    return False
        return True