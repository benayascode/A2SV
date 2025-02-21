# Problem: LRU Cache - https://leetcode.com/problems/lru-cache/

class ListNode:
    def __init__(self,key=-1,val=-1,next=None,prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.mydict = {}
        self.capacity = capacity
        self.head = ListNode()
        self.tail = ListNode()

        self.head.next = self.tail
        self.tail.prev = self.head
        

    def get(self, key: int) -> int:
        if key in self.mydict:
            v = self.mydict[key]
            self.remove(v)
            self.insert(v)
            return v.val
        
        return -1


    def remove(self,node):
        pr = node.prev
        nxt = node.next
        pr.next = nxt
        nxt.prev = pr
        key = node.key
        self.mydict.pop(key)


    def insert(self,node):
        key = node.key
        per_tail = self.tail.prev
        per_tail.next = node
        node.prev = per_tail
        node.next = self.tail
        self.tail.prev = node
        self.mydict[key] = node

    def put(self, key: int, value: int) -> None:
        if key in self.mydict:
            new = self.mydict[key]
            new.val = value
            self.remove(new)

        else:
            new = ListNode(key,value)
            if len(self.mydict) == self.capacity:
                lru = self.head.next
                self.remove(lru)
        self.insert(new)

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)