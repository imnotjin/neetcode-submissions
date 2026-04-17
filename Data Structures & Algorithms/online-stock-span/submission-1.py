class StockSpanner:

    def __init__(self):
        self.stack = []
        self.idx = 0

    def next(self, price: int) -> int:
        if not self.stack:
            self.stack.append((price, self.idx))
            self.idx += 1
            return 1

        new_stack = self.stack[:]
        while new_stack and new_stack[-1][0] <= price:
            new_stack.pop()
        
        self.stack.append((price, self.idx))
        self.idx += 1

        return self.idx - new_stack[-1][1] - 1 if new_stack else self.idx



# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)