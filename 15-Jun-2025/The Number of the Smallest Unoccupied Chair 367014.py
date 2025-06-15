# Problem: The Number of the Smallest Unoccupied Chair - https://leetcode.com/problems/the-number-of-the-smallest-unoccupied-chair/description/

class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        hp = []
        n = len(times)
        
        for ind, (a, l) in enumerate(times):
            hp.append((a, ind, 'start'))
            hp.append((l, ind, 'stop'))
        hp.sort(key=lambda x: (x[0], x[2] == 'start'))

        opn = []
        occ = {}
        curr = 0

        for t, ind, s in hp:
            if s == 'start':
                if opn:
                    chair = heapq.heappop(opn)
                else:
                    chair = curr
                    curr += 1
                occ[ind] = chair
                
                if ind == targetFriend:
                    return chair
            else:  
                chair = occ[ind]
                heapq.heappush(opn, chair)