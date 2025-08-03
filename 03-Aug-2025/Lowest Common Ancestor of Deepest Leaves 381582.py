# Problem: Lowest Common Ancestor of Deepest Leaves - https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node, depth):
            if not node:
                return (None, depth)
            
            left,ld = dfs(node.left, depth+1)
            right, rd = dfs(node.right, depth+1)

            if ld > rd:
                return (left, ld)
            
            elif rd> ld:
                return (right, rd)
            
            else:
                return node,ld

        out,x = dfs(root, 0)
        return out