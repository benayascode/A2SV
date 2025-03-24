# Problem: Count Nodes Equal to Average of Subtree - https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        c = 0

        def rec(root):
            nonlocal c

            if not root:
                return (0,0)
            
            left_sum , left_cnt = rec(root.left)
            right_sum , right_cnt = rec(root.right)

            tot = left_sum + right_sum + root.val
            cnt = left_cnt + right_cnt + 1
            if tot//cnt == root.val:
                c += 1
            return tot,cnt
            
        rec(root)
        return c

        