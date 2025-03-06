# Problem: Score of Parentheses - https://leetcode.com/problems/score-of-parentheses/

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]
        total = 0
        for ch in s:
            if ch == "(":
                stack.append(0)
            else:
                top = stack.pop()
                val = max(1,2*top)
                stack[-1] += val

        return stack.pop()