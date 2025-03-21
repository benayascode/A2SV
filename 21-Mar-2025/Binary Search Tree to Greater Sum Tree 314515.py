# Problem: Binary Search Tree to Greater Sum Tree - https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        arr = []
        def dfs(root):
            if not root:
                return
            
            dfs(root.left)
            arr.append(root.val)
            dfs(root.right)
        dfs(root)
        
        for i in range(len(arr)-2,-1,-1):
            arr[i] += arr[i+1]
        
        i = 0

        def dfs(root):
            nonlocal i
            if not root:
                return
            
            dfs(root.left)
            root.val = arr[i]
            i += 1
            dfs(root.right)
        dfs(root)


        return root