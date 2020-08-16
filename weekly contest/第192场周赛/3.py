from typing import List
import collections
class BrowserHistory:

    def __init__(self, homepage: str):
        self.queue = [homepage]
        self.loc = len(self.queue) - 1


    def visit(self, url: str) -> None:
        if not self.queue:
            self.queue.append(url)
            self.loc = 0
        else:
            if len(self.queue) - 1 == self.loc:
                self.queue.append(url)
                self.loc += 1
            else:
                self.queue[self.loc + 1] = url
                self.queue[self.loc + 2:] = []
                self.loc += 1


    def back(self, steps: int) -> str:
        print(self.queue, self.loc)
        while steps and self.loc > 0:
            steps -=  1
            self.loc -= 1
        return self.queue[self.loc]


    def forward(self, steps: int) -> str:
        print(self.queue, self.loc)
        while steps and self.loc < len(queue) - 1:
            steps -= 1
            self.loc += 1
        return self.queue[self.loc]




# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)