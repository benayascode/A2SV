# Problem: 132 Pattern - https://leetcode.com/problems/132-pattern/

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        st = []
        mini = nums[0]
        nums = nums[1:]

        for i in nums:
            while st and i >= st[-1][0]:
                st.pop()

            if st and i > st[-1][1]:
                return True
            
            st.append([i, mini])
            mini = min(mini, i)
        
        return False