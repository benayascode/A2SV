# Problem: Design Linked List - https://leetcode.com/problems/design-linked-list/

class ListNode:
    def __init__(self,val=-1,next=None):
        self.val = val
        self.next = None


class MyLinkedList:

    def __init__(self):
        self.MyLinkedList = ListNode()

    def get(self, index: int) -> int:
        
        
        curr = self.MyLinkedList
        if index == 0:
            if curr.next:
                return curr.next.val
            return -1
        i = -1
        out = curr.val
        
        while i < index and curr != None :
            i += 1
            # out = curr.val
            curr = curr.next
            out  =  curr.val if curr is not None else -1
        # if out :
        return out
        # else:
        #     return -1


    def addAtHead(self, val: int) -> None:
        # c = self.MyLinkedList
        # while c:
        #     print(c.val)
        #     c = c.next
        new = ListNode(val)
        # if self.MyLinkedList == None:
        #     self.MyLinkedList = dummy
        # else:
        #     dummy.next = self.MyLinkedList
        #     self.MyLinkedList = dummy

        dummy = self.MyLinkedList
        existing_head = dummy.next
        dummy.next = new
        new.next = existing_head

        # while c:
        #     print(c.val)
        #     c = c.next

        

    def addAtTail(self, val: int) -> None:
        c = self.MyLinkedList
        while c.next != None:
            c = c.next
        new =  ListNode(val)
        c.next = new

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
            return
        i = -1
        curr = self.MyLinkedList
        while i < index and curr:
            if i+1 == index:
                x = curr.next
                v = ListNode(val)
                v.next = x
                curr.next = v
                break
            curr = curr.next

            i += 1
       
       

    def deleteAtIndex(self, index: int) -> None:
        if index == 0:
            if self.MyLinkedList.next:
                self.MyLinkedList.next = self.MyLinkedList.next.next
            return
        i = -1
        curr = self.MyLinkedList
        while i < index and curr:
            if i+1 == index:
                if curr.next != None:
                    curr.next = curr.next.next
                # else:
                    # curr.next = None
                break
            curr = curr.next

            i += 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)