# Problem: Minimum Index Sum of Two Lists - https://leetcode.com/problems/minimum-index-sum-of-two-lists/description/

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        mydict = defaultdict(int)
        res = defaultdict(int)

        for i,j in enumerate(list1):
            mydict[j] = i
        
        for i,j in enumerate(list2):
            if j in mydict:
                res[j] = (mydict[j]+i)
        res = dict(sorted(res.items() , key = lambda x:x[1]))
        mini = min(list(res.values()))
        out = []
        for i in res:
            if res[i] != mini:
                break
            else:
                out.append(i)
        return out
        
        



        