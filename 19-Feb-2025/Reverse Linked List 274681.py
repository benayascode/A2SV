# Problem: Reverse Linked List - https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        out = ListNode(0)
        cur = out
        stack = []
        while head:
            stack.append(head)
            head = head.next
        while stack:    
            cur.next = stack.pop()
            cur = cur.next
        if cur:
            cur.next = None
        return out.next