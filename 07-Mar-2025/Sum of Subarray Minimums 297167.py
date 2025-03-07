# Problem: Sum of Subarray Minimums - https://leetcode.com/problems/sum-of-subarray-minimums/

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:

        st = []
        ans = 0
        for i in arr:
            c = 0
            while st and st[-1][0] > i:
                l = st[-1][1]
                r = c
                ans += ((l+1) * (r+1))*st[-1][0]
                c += (1+st[-1][1])
                st.pop()
            
            st.append([i,c])

        print(ans)
        n = len(st)

        right = 0
        for i in range(n-1,-1,-1):
            left = st[i][1]
            ans += (left + 1) * (right + 1) * st[i][0]
            right += (1 + st[i][1])

        
        

        return ans % (10**9 + 7)
             
        