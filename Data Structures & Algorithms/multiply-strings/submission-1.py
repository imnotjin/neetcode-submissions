class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def to_int(num):
            res = 0
            for i, digit in enumerate(num):
                res += (ord(digit) - ord('0')) * 10 ** (len(num) - i - 1)
            return res

        return str(to_int(num1) * to_int(num2))
