# Problem: Sort List - https://leetcode.com/problems/sort-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        out = []
        dummy = ListNode()
        cur = head
        c = dummy
        while cur:
            out.append(cur.val)
            cur = cur.next
        out.sort()
        for value in out:
            c.next = ListNode(value)  
            c = c.next  
        return dummy.next