# Problem: Reverse Odd Levels of Binary Tree - https://leetcode.com/problems/reverse-odd-levels-of-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return []
        out = []
        queue = deque([root])
        f = 0

        while queue:
            l = len(queue)
            if f and 1:
                left,right = 0 , l-1
                while left < right:
                    queue[right].val,queue[left].val = queue[left].val,queue[right].val
                    right -= 1
                    left += 1
                f = 0
            else:
                f = 1
          
            l = len(queue)
            
            for i in range(l):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            

           
        return root