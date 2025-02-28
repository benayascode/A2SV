# Problem: Design Browser History - https://leetcode.com/problems/design-browser-history/description/

class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.stack = []

    def visit(self, url: str) -> None:
        self.history.append(url)
        self.stack = []

    def back(self, steps: int) -> str:
        while steps > 0 and len(self.history) > 1:
            self.stack.append(self.history.pop())
            steps -= 1
        return self.history[-1]
        

    def forward(self, steps: int) -> str:
        while steps > 0 and self.stack:
            self.history.append(self.stack.pop())
            steps -= 1
        return self.history[-1]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)