# Problem: Partition List - https://leetcode.com/problems/partition-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        lower_val = ListNode(0) 
        higher_val = ListNode(0)  

        low = lower_val
        up = higher_val

        while head:
            if head.val < x:
                low.next = head
                low = low.next
            else:
                up.next = head
                up = up.next
            head = head.next

        low.next = higher_val.next
        up.next = None

        return lower_val.next
        
        

