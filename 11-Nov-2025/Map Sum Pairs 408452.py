# Problem: Map Sum Pairs - https://leetcode.com/problems/map-sum-pairs/description/

class TrieNode:
    def __init__(self):
        self.children = {}
        self.cnt = 0


class MapSum:

    def __init__(self):
        self.root = TrieNode()
        self.mydict = {}
        

    def insert(self, key: str, val: int) -> None:
        x = val
        if key in self.mydict:
            x = val - self.mydict[key]
        self.mydict[key] = val
        curr = self.root
        for i in key:
            if i not in curr.children:
                curr.children[i] = TrieNode()
            curr = curr.children[i]
            curr.cnt += x

        

    def sum(self, prefix: str) -> int:
        curr = self.root
        for i in prefix:
            if i not in curr.children:
                curr.children[i] = TrieNode()
            curr = curr.children[i]
        return curr.cnt
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)