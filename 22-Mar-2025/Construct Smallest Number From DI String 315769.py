# Problem: Construct Smallest Number From DI String - https://leetcode.com/problems/construct-smallest-number-from-di-string/description/

class Solution:
    def smallestNumber(self, pattern: str) -> str:
        out = []
        st = []
        for i in range(len(pattern)+1):
            st.append(str(i+1))
            if i == len(pattern) or pattern[i] == 'I':
                while st:
                    out.append(st.pop())
        return "".join(out)