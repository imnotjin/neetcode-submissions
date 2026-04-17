class Solution:
    def reverse(self, x: int) -> int:
        string = str(x)[::-1] if x >= 0 else "-" + str(x)[1:][::-1]
        if -2 ** 31 <= int(string) <= 2 ** 31 - 1:
            return int(string)
        else:
            return 0
            