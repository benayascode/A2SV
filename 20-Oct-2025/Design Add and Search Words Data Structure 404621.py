# Problem: Design Add and Search Words Data Structure - https://leetcode.com/problems/design-add-and-search-words-data-structure/

class TrieNode:
    def __init__(self):
        self.children = {}
        self.flag = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for i in word:
            if i not in curr.children:
                curr.children[i] = TrieNode()
            curr = curr.children[i]
        curr.flag = True
        

    def search(self, word: str) -> bool:
        def dfs(node, ind):
            if ind == len(word):
                return node.flag
            if word[ind] == ".":
                for i in node.children.values():
                    if dfs(i, ind+1):
                        return True
            
            if word[ind] in node.children:
                return dfs(node.children[word[ind]], ind+1)
        
            return False
        return dfs(self.root, 0)
            


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)