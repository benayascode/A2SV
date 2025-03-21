# Problem: Binary Tree Zigzag Level Order Traversal - https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        out = []
        queue = deque([root])
        f = 0

        while queue:
            row = []
            l = len(queue)
            
            for i in range(l):
                node = queue.popleft()
                row.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if f:
                row.reverse()
                f = 0
            else:
                f = 1

            out.append(row)
        return out
                
        