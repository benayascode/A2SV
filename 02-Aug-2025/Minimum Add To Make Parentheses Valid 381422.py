# Problem: Minimum Add To Make Parentheses Valid - https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        st = []
        c = 0
        for i in s:
            if i == "(":
                st.append(i)
            else:
                if st:
                    st.pop()
                else:
                    c += 1
        return c + len(st)