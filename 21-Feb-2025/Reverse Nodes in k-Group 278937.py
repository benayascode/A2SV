# Problem: Reverse Nodes in k-Group - https://leetcode.com/problems/reverse-nodes-in-k-group/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        holder, seeker = head, head
        dummy = ListNode(0, head)

        last_head = dummy

        while True:

            # phase 1: find the k consecutive nodes
            count = 0
            while count < k and seeker:
                seeker = seeker.next
                count += 1
            

            if count < k:
                return dummy.next
            
            nxt = seeker
            next_last_head = holder

            while count:
                temp = holder.next
                holder.next = nxt
                nxt = holder
                holder = temp
                count -= 1
            
            last_head.next = nxt
            last_head = next_last_head
            

