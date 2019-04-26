class StockSpanner:
    def __init__(self):
        self.prices = []
        self.stack = []
        self.i = 0

    def next(self, price: int) -> int:
        # if not self.stack:return 1
        while self.stack and self.prices[self.stack[-1]] <= price:
            self.stack.pop()
        self.prices.append(price)
        self.stack.append(self.i)
        self.i += 1
        return (
            self.stack[-1] - self.stack[-2]
            if len(self.stack) > 1
            else self.stack[-1] + 1
        )


a = StockSpanner()
print(a.next(100))
print(a.prices)
print(a.stack)
print(a.next(80))
print(a.next(60))
print(a.next(70))
# print(a.prices)
# print(a.stack)
print(a.next(60))
print(a.next(75))
print(a.next(85))
