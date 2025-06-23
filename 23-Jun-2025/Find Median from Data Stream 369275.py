# Problem: Find Median from Data Stream - https://leetcode.com/problems/find-median-from-data-stream/

class MedianFinder:

    def __init__(self):
        self.nums = []
        self.s = 0

    def addNum(self, num: int) -> None:
        bisect.insort(self.nums,num)
        self.s += 1

        

    def findMedian(self) -> float:
        if (self.s) % 2:return self.nums[self.s//2]
        return (self.nums[self.s//2]+self.nums[self.s//2-1])/2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()