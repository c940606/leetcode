class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self. c = 0
        self.n = n
        self.lookup = {}
        self.discount = discount
        for idx, p in zip(products, prices):
            self.lookup[idx] = p


    def getBill(self, product: List[int], amount: List[int]) -> float:
        if self.c != self.n:
            cur = 0
            for idx, num in zip(product, amount):
                cur += self.lookup[idx] * num
            self.c += 1
            return cur
        else:
            self.c = 0
            cur = 0
            for idx, num in zip(product, amount):
                cur += self.lookup[idx] * num
            cur -= (cur * self.discount) / 100
            return cur



# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)