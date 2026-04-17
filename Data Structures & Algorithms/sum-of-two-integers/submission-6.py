class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = (1 << 32) - 1

        while b & mask:
            carry = (a & b) << 1
            a = a ^ b
            b = carry

        return a if b == 0 else a & mask
