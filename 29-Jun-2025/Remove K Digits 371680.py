# Problem: Remove K Digits - https://leetcode.com/problems/remove-k-digits/

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        st = [num[0]]
        for i in range(1,len(num)):
            x = num[i]
            while st and st[-1] > x and k:
                st.pop()
                k -= 1
            
            st.append(x)

        while k:
            k -= 1
            st.pop()

        s = "".join(st).lstrip("0")
        return s if s else "0"
        