# Problem: Two City Scheduling - https://leetcode.com/problems/two-city-scheduling/

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costa = 0
        costb = 0
        # print(costa,costb)

        costs.sort(key = lambda x:(x[0]-x[1]))
        # print(costs)
        
        for i in range(len(costs)//2):
            costa += costs[i][0]     

        for i in  range(len(costs)//2,len(costs)):
            costa += costs[i][1]
        

        return costa
        
       