class Solution:
    def next(self, n):
        total = 0
        while n > 0:
            total += (n % 10) ** 2
            n //= 10
        return total

    def isHappy(self, n: int) -> bool:
        slow, fast = n, n

        while True:
            slow = self.next(slow)
            fast = self.next(self.next(fast))

            if slow == 1:
                return True
            if slow == fast:
                return False

        return False
                