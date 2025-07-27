# Problem: Sort the Jumbled Numbers - https://leetcode.com/problems/sort-the-jumbled-numbers/

class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        mydict = {}
        for i in nums:
            if i in mydict:
                continue
            dig = map(int,str(i))
            # for n in dig:
            #     print(n)
            x = "".join(str(mapping[n]) for n in dig)
            mydict[i] = int(x)
        return sorted(nums, key=mydict.get)
