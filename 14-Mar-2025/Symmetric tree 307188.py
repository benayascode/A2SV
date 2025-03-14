# Problem: Symmetric tree - https://leetcode.com/problems/symmetric-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        res_left = []
        rootl = root.left
        rootr = root.right
        def dfsleft(root):
            if not root:
                res_left.append("*")
                return None
            res_left.append(root.val)
            dfsleft(root.left)
            dfsleft(root.right)

            return res_left
        
        res_right = []
        def dfsright(root):
            if not root:
                res_right.append("*")
                return None

            res_right.append(root.val)
            dfsright(root.right)
            dfsright(root.left)

            return res_right
        print(dfsleft(rootl) , dfsright(rootr))
        return dfsleft(rootl) == dfsright(rootr)