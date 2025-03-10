# Problem: Reveal cards in increasing order  - https://leetcode.com/problems/reveal-cards-in-increasing-order/

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        n  = len(deck)
        st = deque()
        st.append(deck[n - 1])
        for i in range(n-2,-1,-1):
            st.appendleft(st.pop())
            st.appendleft(deck[i])
            # print(st)

        out = []
        while st:
            out.append(st.popleft())
        return out
        
            

