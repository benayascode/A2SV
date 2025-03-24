# Problem: Convert Sorted Array to Binary Search Tree - https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def rec(arr):
            n = len(arr)
            if not arr:
                return
            
            node = TreeNode(arr[n//2])
            node.left = rec(arr[:n//2])
            node.right = rec(arr[n//2+1:])

            return node
        
        return rec(nums)
        
