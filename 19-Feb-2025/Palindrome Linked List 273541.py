# Problem: Palindrome Linked List - https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        st = []
        out = head
        cur = head
        while cur:
            st.append(cur.val)
            cur = cur.next
        while out:
            if out.val != st.pop():
                return False
            out = out.next
        return True