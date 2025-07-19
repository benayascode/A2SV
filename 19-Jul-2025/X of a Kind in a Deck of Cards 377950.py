# Problem: X of a Kind in a Deck of Cards - https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards/

class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        mydict = Counter(deck).values()
        x = 0
        for i in mydict:
            x = gcd(x,i)
        return x >= 2

        