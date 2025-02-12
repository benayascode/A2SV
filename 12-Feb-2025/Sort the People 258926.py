# Problem: Sort the People - https://leetcode.com/problems/sort-the-people/

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
    
        # bubble
        for j in range(len(heights)):
            for i in range(1,len(heights)-j):
                if heights[i] > heights[i-1]:
                    heights[i],heights[i-1]=heights[i-1],heights[i]
                    names[i],names[i-1]=names[i-1],names[i]
        return names


        
