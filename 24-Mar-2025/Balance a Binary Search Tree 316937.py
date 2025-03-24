# Problem: Balance a Binary Search Tree - https://leetcode.com/problems/balance-a-binary-search-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        arr = []
        def inord(root):
            nonlocal arr
            if not root:
                return
            
            inord(root.left)
            arr.append(root.val)
            inord(root.right)

            return arr
        inord(root)
        # print(arr)

        def rec(arr):
            n = len(arr)
            if not arr:
                return
            
            node = TreeNode(arr[n//2])
            node.left = rec(arr[:n//2])
            node.right = rec(arr[n//2+1:])

            return node
        
        return rec(arr)





