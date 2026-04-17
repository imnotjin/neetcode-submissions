class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def convert(num):
            res = 0
            for i, digit in enumerate(num):
                res += (ord(digit) - 48) * 10 ** (len(num) - i - 1)
            return res

        return str(convert(num1) * convert(num2))
