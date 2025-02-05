# Problem: Find All Duplicates in an Array - https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        mydict = {}
        out = []
        for i in nums:
            if i in mydict:
                mydict[i] += 1
                if mydict[i] == 2:
                    out.append(i)
            else:
                mydict[i] = 1
        return out