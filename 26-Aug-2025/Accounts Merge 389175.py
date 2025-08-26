# Problem: Accounts Merge - https://leetcode.com/problems/accounts-merge/

class UF:
    def __init__(self, n):
        self.parents = list(range(n))
    def union(self, child, parent):
        self.parents[self.find(child)] = self.find(parent)
    def find(self, x):
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UF(len(accounts))
        mydict = {}
        for i, j in enumerate(accounts):
            eml = j[1:]
            for k in eml:
                if k in mydict:
                    uf.union(i, mydict[k])

                mydict[k] = i
    
        out = defaultdict(list)
        
        for x, y in mydict.items():
            out[uf.find(y)].append(x)
        res = []
        
        for i, j in out.items():
            name = accounts[i][0]     
            merged = [name] + sorted(j) 
            res.append(merged)

        return res