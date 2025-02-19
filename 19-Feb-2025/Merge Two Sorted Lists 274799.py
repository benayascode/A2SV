# Problem: Merge Two Sorted Lists - https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]: 
        dummy = ListNode()
        out = dummy
        cur1 = list1
        cur2 = list2

        while cur1 and cur2:
            if cur1.val < cur2.val:
                out.next = cur1
                cur1 = cur1.next
            else:
                out.next = cur2
                cur2 = cur2.next
            out = out.next
            
        if cur1:
            out.next = cur1
        else:
            out.next = cur2

        return dummy.next