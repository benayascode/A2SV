# Problem: Top K Frequent Words - https://leetcode.com/problems/top-k-frequent-words/

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        words.sort()
        mydict = Counter(words)
        out = nlargest(k, mydict, key = mydict.get)
        return out
        