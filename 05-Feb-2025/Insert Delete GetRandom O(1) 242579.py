# Problem: Insert Delete GetRandom O(1) - https://leetcode.com/problems/insert-delete-getrandom-o1/description/

class RandomizedSet:

    def __init__(self):
        self.list = []
        self.mydict = {}

    def insert(self, val: int) -> bool:
        if val not in self.mydict:
            self.mydict[val] = len(self.list)
            self.list.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.mydict:
            i = self.mydict[val]
            last_val = self.list[-1]
            self.list[i] = last_val
            self.mydict[last_val] = i
            self.list.pop()
            del self.mydict[val]
            return True
        
        return False


    def getRandom(self) -> int:
        return random.choice(self.list)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()