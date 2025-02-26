# Problem: Maximum Twin Sum of a Linked List - https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        fast = head
        slow = head
        stack = []
        while fast:
            stack.append(slow.val)
            slow=slow.next
            fast = fast.next.next
        out = 0
        while slow:
            out = max(out,slow.val+stack.pop())
            slow = slow.next
        return out