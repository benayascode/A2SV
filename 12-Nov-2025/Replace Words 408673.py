# Problem: Replace Words - https://leetcode.com/problems/replace-words/

class TrieNode:
    def __init__(self):
        self.children = {}
        self.flag = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root

        for i in word:
            if i not in curr.children:
                curr.children[i] = TrieNode()
            curr = curr.children[i]
        curr.flag += 1

    def change(self, w):
        curr = self.root
        ind = 0
        for i in w:
            if i not in curr.children:
                return w
            curr = curr.children[i]
            ind += 1
            if curr.flag:
                return w[:ind]
        return w

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        root = Trie()
        for i in dictionary:
            root.insert(i)
        out = []
        for i in sentence.split():
            out.append(root.change(i))
        return ' '.join(out)