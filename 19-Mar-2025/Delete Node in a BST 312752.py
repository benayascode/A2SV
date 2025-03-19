# Problem: Delete Node in a BST - https://leetcode.com/problems/delete-node-in-a-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
            
        if root.val > key:
            root.left = self.deleteNode( root.left, key )

        elif root.val < key:
            root.right = self.deleteNode( root.right, key )

        else:
            if (not root.left) or (not root.right):
                if root.right:
                    root = root.right  
                else:
                    root = root.left

            else:
                out = root.right
                while out.left:
                    out = out.left
                root.val = out.val
                root.right = self.deleteNode( root.right, out.val )
                    
        return root