# Problem: Product of the Last K Numbers - https://leetcode.com/problems/product-of-the-last-k-numbers/description/

class ProductOfNumbers:

    def __init__(self):
        self.pre = []
        self.l = 0
        self.zero = -1
        

    def add(self, num: int) -> None:
        
        if num == 0:
            self.zero = self.l
        self.pre.append(num)
        self.l += 1
        if self.l > 1 and self.pre[self.l-2] != 0:
            self.pre[self.l-1] *= self.pre[self.l-2]
        

    def getProduct(self, k: int) -> int:
        if k == self.l:
            if self.zero == -1:
                return self.pre[-1]
            else:
                return 0

            # return self.pre[0]
        if (self.l-k) <= self.zero:
            return 0
        if (self.l-k - 1) == self.zero:
            return self.pre[-1]
        return self.pre[-1] // self.pre[-k - 1] 
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)