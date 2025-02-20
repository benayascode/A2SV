# Problem: Remove Nth Node From End of List - https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        k = -1
        dummy.next = head
        cur = dummy

        while cur:
            k += 1
            cur = cur.next

        l = k - n
        i = 0
        cur = dummy
        while cur:
            if i == l:
                cur.next = cur.next.next
                return dummy.next
            cur = cur.next
            i += 1
            