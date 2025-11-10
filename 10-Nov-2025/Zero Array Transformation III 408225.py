# Problem: Zero Array Transformation III - https://leetcode.com/problems/zero-array-transformation-iii/description/

class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        heap = []

        mydict = defaultdict(list)

        for i, j in queries:
            mydict[i].append(j)

        arr = [0] * (len(nums) + 1)
        x = 0
        for i in range(len(nums)):
            x += arr[i]

            for j in mydict[i]:
                heapq.heappush(heap, -j)
            
            
            while heap and x < nums[i]:
                temp = heapq.heappop(heap)
                if -temp < i: continue
                arr[-temp + 1] -= 1
                x += 1
                
            if not heap and x < nums[i]: return -1
        
        return len(heap)