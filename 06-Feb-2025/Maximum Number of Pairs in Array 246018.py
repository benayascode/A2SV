# Problem: Maximum Number of Pairs in Array - https://leetcode.com/problems/maximum-number-of-pairs-in-array/description/

class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        mydict = Counter(nums)
        a , b = 0 , 0
        for i in mydict:
            if mydict[i] % 2:
                b += 1
            a += (mydict[i] // 2)
        return [a,b]
            


        