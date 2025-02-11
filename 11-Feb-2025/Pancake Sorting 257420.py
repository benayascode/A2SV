# Problem: Pancake Sorting - https://leetcode.com/problems/pancake-sorting/

class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        out = []
        def flip(k):
            s = 0
            while s < k:
                arr[s],arr[k] = arr[k],arr[s]
                s += 1
                k -= 1
        for i in range(len(arr)-1,0,-1):
            maxi = i
            for j in range(i,-1,-1):
                if arr[j] > arr[maxi]:
                    maxi = j
            if maxi != i:
                flip(maxi)
                flip(i)
                out.append(maxi+1)
                out.append(i+1)
        return out

        