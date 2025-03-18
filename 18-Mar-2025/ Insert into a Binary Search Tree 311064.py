# Problem:  Insert into a Binary Search Tree - https://leetcode.com/problems/insert-into-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        if not root:
            return TreeNode(val)
        out = root
        while root:
            if root.val < val:
                if root.right:
                    root = root.right
                    continue
                else:
                    root.right = TreeNode(val)
                    break
            if root.val > val:
                if root.left:
                    root = root.left
                    continue
                else:
                    root.left = TreeNode(val)
                    break
        return out
