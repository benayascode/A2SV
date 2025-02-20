# Problem: Remove Duplicates from Sorted List - https://leetcode.com/problems/remove-duplicates-from-sorted-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode("a")
        dummy.next = head
        curr = dummy

        val = curr.val
        while curr.next:
            if curr.next.val != val:
                val = curr.next.val
                curr = curr.next
            else:
                curr.next = curr.next.next

        return dummy.next