# Problem: Find Consecutive Integers from a Data Stream - https://leetcode.com/problems/find-consecutive-integers-from-a-data-stream/

class DataStream:

    def __init__(self, value: int, k: int):
        self.val = value
        self.k = k
        self.l = 0
        self.r = 0


    def consec(self, num: int) -> bool:
        self.r += 1
        if self.val != num:
            self.l = self.r
        return self.r-self.l >= self.k   
        

# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)
