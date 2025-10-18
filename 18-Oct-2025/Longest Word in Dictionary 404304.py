# Problem: Longest Word in Dictionary - https://leetcode.com/problems/longest-word-in-dictionary/

class Solution:
    class TrieNode:
        def __init__(self):
            self.children = {}
            self.flag = False

    def __init__(self):
        self.root = self.TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for i in word:
            if i not in curr.children:
                curr.children[i] = self.TrieNode()
            curr = curr.children[i]
        curr.flag = True        

    def search(self, word: str) -> bool:
        curr = self.root
        for i in word:
            if i not in curr.children:
                return False
            curr = curr.children[i]
        return curr.flag

    def longestWord(self, words: List[str]) -> str:
        for i in words:
            self.insert(i)

        out = []
        for w in words:
            x = 0
            t = ""
            for i in w:
                t += i
                if not self.search(t):
                    x = 1
                    break
            if x == 0:
                out.append(w)
        if not out:
            return ""
        return max(sorted(out), key=lambda x: len(x))

